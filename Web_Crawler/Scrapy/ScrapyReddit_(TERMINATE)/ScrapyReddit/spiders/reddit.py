# 執行爬蟲: scrapy crawl <reddit>
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "reddit" # 蜘蛛的名字，scrapy list 可以看到所有可用的 spider
    
    allowed_domains = ['reddit.com'] # 限制爬蟲的作用域：爬蟲只會嘗試爬取屬於這些域名的網頁。

    start_urls = [ # 爬蟲的起始點：包含了初始請求的 URL list。並將 Response 傳遞給 parse 方法進行處理。
        "https://www.reddit.com/r/EsgInvesting/"
    ] 


    def parse(self, response): # response 是 Scrapy 的 Response object，包含了伺服器返回的 HTML 內容以及相關的元數據。
        # XPath will return SelectorList Object
        # extract() return a list
        # extract_first() return the first element in the list in str format. 

        # 主頁 link
        posts = response.xpath('//article[@class="w-full m-0"]') # SelectorList Object
        for post in posts:
            links = response.xpath('.//a[@slot="full-post-link" and @class="absolute inset-0"]/@href').extract()
            
            for link in links:
                # 使用內建方法 response.urljoin(link) 將相對路徑轉換為絕對路徑，Scrapy 的 response 對象中自帶 url 屬性
                # URL : https://www.reddit.com/，而 link = "/r/Python/comments/abc123"
                # 結果為 https://www.reddit.com/r/Python/comments/abc123
                ab_url = response.urljoin(link)

                # scrapy.Request 創建一個新的 HTTP 請求，並將這個請求添加到內部的 Scheduler 隊列中等待執行。
                # callback: 指定當請求的 response 返回時，由哪個函數處理這個響應。
                # callback=self.parse_detail：return response 後，執行 parse_detail 
                yield scrapy.Request(ab_url, callback=self.parse_detail) # 異步操作，不會立即執行所以沒必要賦值給Variable.

        next_page = response.xpath('//a[@rel="nofollow next"]/@href').extract_first()  # 下一頁URL
        if next_page:
            next_page_url = response.urljoin(next_page) 
            yield scrapy.Request(next_page_url, callback=self.parse)



    def parse_detail(self, response):  # callback
        title = response.xpath('//h1/text()').extract_first()  
        content = response.xpath('//div[@class="content"]//text()').extract()  

        yield {  
            'title': title,        # 標題
            'content': content,    # 正文
            'url': response.url    # 文章的完整 URL
        }

'''
spider 每抓取到一個 item 後，便會送到 Item Pipeline ，經過多個元件依序串起來成為一個資料處理的管線。(pipelines.py)
'''


# 補充
'''
在爬蟲中，將相關的數據(如 TITLE、DATE 和 LINK) 按照「每篇文章」的單位匹配和存儲是關鍵。
如果處理不當，可能會導致數據混亂（例如: TITLE 和 DATE 對不上）。
Scrapy 中的做法是通過定位共同的父節點，然後在這個範圍內提取每篇文章的數據，確保不同數據對應於同一篇文章。

1. 選擇所有文章父節點
//div[@class="post"] # 假設為 class='post' 為區分每篇文章的父節點

2. 從父節點內提取數據
.//a[@class="title"]/text() # .// 表示從當前的父節點查找
.//a[@class="title"]/@href
.//time/@datetime


3. code 範例

def parse(self, response):
    posts = response.xpath('//div[@class="post"]') # 會抓出匹配的所有 SelectorList Object
    
    for post in posts:
        title = post.xpath('.//a[@class="title"]/text()').extract_first()
        link = post.xpath('.//a[@class="title"]/@href').extract_first()
        date = post.xpath('.//time/@datetime').extract_first()

'''

