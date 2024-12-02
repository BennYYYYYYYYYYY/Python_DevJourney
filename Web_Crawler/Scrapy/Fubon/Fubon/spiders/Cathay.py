# scrapy shell url
# it will return a response object

import scrapy
from Fubon.items import FubonItem


class CathaySpider(scrapy.Spider):
    name = "Cathay"
    allowed_domains = ["cathay-ins.com.tw"]
    start_urls = [
        "https://www.cathay-ins.com.tw/cathayins/personal/knowledge-blog/category-01/",
        "https://www.cathay-ins.com.tw/cathayins/personal/knowledge-blog/category-02/",
        "https://www.cathay-ins.com.tw/cathayins/personal/knowledge-blog/category-03/"
    ]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,  # 禁用 robots.txt 規則
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',  # 自定義 User-Agent
        'DOWNLOAD_DELAY': 0.5,  # 設置下載延遲，避免被檢測到為爬蟲
        'CONCURRENT_REQUESTS': 4,  # 限制同時請求數
    }

    item = FubonItem()
    def parse(self, response):
        posts = response.xpath('//div[contains(@id,"layout_0_content_1_Rpt_BlogArticle_AddingVideoIcon")]')
        for post in posts:
            link = post.xpath('.//div[@class="cathay-feeditem"]/a/@href').get()
            
            yield response.follow(
                link,
                callback = self.parse_info
            )

    def parse_info(self, response):
        title = response.xpath("//div[@class='cathay-article-maintitle']/h1[@id='layout_0_content_1_MainTitle']/text()").get()
        date = response.xpath("//div[@class='cathay-article-maintitle']/div[@id='layout_0_content_1_ArticleDateAndTag' and contains(@class, 'cathay-article-meta')]/text()").get()
        item = {
            "title":title,
            "date":date,
            "link":response.url
        }

        yield item
