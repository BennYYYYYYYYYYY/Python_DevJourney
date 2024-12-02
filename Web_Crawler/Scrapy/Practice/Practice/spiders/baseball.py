import scrapy

# spider one: PPT baseball 版
class BaseballSpider(scrapy.Spider):
    name = "baseball"
    allowed_domains = ["ptt.cc"]
    start_urls = ["https://www.ptt.cc/bbs/baseball/index.html"]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 這樣就不用直接改 settings.py
    }


    def parse(self, response):
        posts = response.xpath('//div[@class="r-ent"]')
        for post in posts:
            title = post.xpath('./div[@class="title"]/a/text()').extract()
            author = post.xpath('./div[@class="meta"]/div[@class="author"]/text()').extract()
            baseball_item = {
                'title':title,
                'author':author
            }

        yield baseball_item
        




