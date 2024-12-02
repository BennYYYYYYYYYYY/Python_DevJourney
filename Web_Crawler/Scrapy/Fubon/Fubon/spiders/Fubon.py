import scrapy
from Fubon.items import FubonItem

class FubonSpider(scrapy.Spider):
    name = "Fubon"
    allowed_domains = ["fubon.com"]
    start_urls = ["https://www.fubon.com/insurance/blog/lifestyle/index.html"]

    custom_settings = {
        'DOWNLOAD_DELAY': 0.3,  # 這樣就不用直接改 settings.py
    }

    item = FubonItem()
    def parse(self, response):
        posts = response.xpath('//div[@class="col-12 col-sm-6 col-md-4"]')
        for post in posts:
            link = post.xpath('.//a/@href').get()
            
            yield response.follow(
                link,
                callback = self.parse_info
            )

    def parse_info(self, response):
        title = response.xpath("//main[@class='col-lg-9']/h1/text()").get()
        date = response.xpath("//main[@class='col-lg-9']/span[@class='date']/text()").get()
        item = {
            "title":title,
            "date":date,
            "link":response.url
        }

        yield item


# 可以在 terminal 中測試 xpath 有沒有命中
''' scrapy shell "url" '''

# 啟動後 Scrapy 會加載指定的 URL 並返回 response 對象，就可以進行操作了
'''
response.xpath("//h1/text()").get()  # 測試 XPath 提取數據
response.css("h1::text").get()      # 測試 CSS 提取數據
response.url                       # 查看加載的 URL
response.status                    # 查看 HTTP 狀態碼
response.body                      # 查看網頁的完整 HTML 源碼
'''
