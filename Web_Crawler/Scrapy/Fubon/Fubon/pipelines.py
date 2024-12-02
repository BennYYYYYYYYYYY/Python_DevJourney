# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import csv

class CSVPipeline:
    # open_spider(): Scrapy Pipeline 的特殊方法，會在蜘蛛開始時被自動調用。
    def open_spider(self, spider): # spider 是 Scrapy 自動傳入的參數，表示當前的蜘蛛對象
        self.fields = ["title", "date", "link"] # 指定 header
        self.file = open('output.csv', 'w', newline='', encoding='utf-8-sig')
        self.writer = csv.DictWriter(self.file, fieldnames=self.fields) # fieldname 定義行的順序，來自 self.fields
        self.writer.writeheader() # 將 filedname 作為 header 寫入 CSV 
        self.batch = []  # 用來暫存數據
        self.batch_size = 100  # 每 100 條數據寫入一次


    # process_item: Scrapy Pipeline 的另一個特殊方法，當 Scrapy 爬取到一個 item 時，這個方法會被自動調用來處理該數據。
    def process_item(self, item, spider):
        for field in self.fields:
            item.setdefault(field, "")  # 如果字典中沒有 field key 就補充成 ""

        self.batch.append(item) # 暫存數據，放到 list

        if len(self.batch) >= self.batch_size: # 暫存的數據量達到 100 時，觸發寫入
            self.writer.writerows(self.batch) # 把 list of dictonary 數據寫入
            self.batch = []  # 清空 list
        return item # Scrapy Pipeline 的約定，讓 Scrapy 將當前 item 傳遞給下一個 Pipeline，或標記該 item 已完成處理。
    

    # close_spider: 蜘蛛執行結束時被自動調用。
    def close_spider(self, spider):
        if self.batch: # 還有剩的話繼續寫入，沒有的話 close
            self.writer.writerows(self.batch)
        self.file.close()




import pandas as pd

class ExcelPipeline:
    def open_spider(self, spider):
        self.items = [] 

    def process_item(self, item, spider):
        self.items.append({
            'title': item['title'],  # 修改為你的實際欄位名稱
            'date': item['date'],
            'link': item['link'],
        })
        return item  # 記得回傳 item，讓其他 pipeline 繼續處理


    def close_spider(self, spider):
        df = pd.DataFrame(self.items) # 爬蟲結束後，將暫存的資料轉為 DataFrame 

        # 使用 ExcelWriter 儲存為 Excel 檔案
        with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)  
