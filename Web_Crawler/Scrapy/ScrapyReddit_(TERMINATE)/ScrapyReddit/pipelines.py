# Pipeline 是一個專門處理爬取數據的模組。它的功能類似於 ETL 流程中的「數據清洗與保存階段」。
'''
Pipeline 的運作方式：數據流過每個階段時，會按照定義的邏輯進行處理。
1. 爬蟲從網頁抓取數據，生成 Item。
2. Scrapy 把 Item 傳給第一個 Pipeline。
3. Pipeline 根據邏輯處理數據，比如清理價格、去掉無效值。
4. 數據流入下一個 Pipeline，繼續加工，直到完成處理並保存。


Pipeline 的設計思路：
1. 每個 Pipeline 負責處理一種特定的邏輯，分而治之。
2. 支持多個 Pipeline 組合使用，按照順序執行。


Pipeline 是 Scrapy 中的一個 Class，主要有三個階段：
1. open_spider：在爬蟲開始時執行，適合初始化資料庫連接或文件操作。
2. process_item：核心方法，負責處理每一條數據。
3. close_spider：在爬蟲結束時執行，用於關閉連接或保存文件。

'''

import csv

class BatchCSVSavePipeline:
    # open_spider
    def open_spider(self, spider):
        self.file = open('output.csv', 'w', newline='', encoding='utf-8')
        self.writer = None
        self.batch = []  # 用來暫存數據
        self.batch_size = 100  # 每 100 條數據寫入一次


    # process_item
    def process_item(self, item, spider):
        # 如果還沒定義欄位名稱，動態生成
        if not self.writer:
            self.fields = list(item.keys())
            self.writer = csv.DictWriter(self.file, fieldnames=self.fields)
            self.writer.writeheader()

        # 暫存數據
        self.batch.append(item)

        # 如果達到批量大小，寫入 CSV
        if len(self.batch) >= self.batch_size:
            self.writer.writerows(self.batch)
            self.batch = []  # 清空批次
        return item


    # close_spider
    def close_spider(self, spider):
        # 爬蟲結束時，寫入剩餘的數據
        if self.batch:
            self.writer.writerows(self.batch)
        self.file.close()




from scrapy.exceptions import DropItem

# 每當Pipeline接收到一篇文章時，便去判斷它是否為空值。
# 若為空值則透過DropItem()這個處理例外的方法將Item去掉，若有值再回傳item。
class DeleteNullTitlePipeline():
    def process_item(self, item, spider):
        title = item['title'] 
        if title:
            return item
        else:
            raise DropItem('found null title %s', item)



# 過濾重複的資料：若發現title已經存在於集合內則丟棄該item，否則丟入集合內並傳回item。
class DuplicatesTitlePipeline():
    def __init__(self):
        self.article = set()
    def process_item(self, item, spider):
        title = item['title'] 
        if title in self.article:
            raise DropItem('duplicates title found %s', item)
        self.article.add(title)
        return(item)
    


'''
啟用 Pipeline：將自定義的 Pipeline 添加到 settings.py 
(把 ITEM_PIPELINES 註解拿掉，並替換成新做的class)

ITEM_PIPELINES = {
   "ScrapyReddit.pipelines.BatchCSVSavePipeline": 300,  # 這裡的數字越小，代表優先級越高，因為可能有好幾個 pipeline
   "ScrapyReddit.pipelines.DeleteNullTitlePipeline": 200,  
   "ScrapyReddit.pipelines.DuplicatesTitlePipeline": 100,  
}

'''


