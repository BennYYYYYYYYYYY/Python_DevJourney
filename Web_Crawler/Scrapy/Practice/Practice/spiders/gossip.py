import scrapy

# ptt gossip 版
class GossipSpider(scrapy.Spider):
    name = "gossip"
    allowed_domains = ["ptt.cc"]
    start_urls = ["https://www.ptt.cc/bbs/gossiping/index.html"]

    def parse(self, response): # 由於 Gossip 版需要加入 COOKIES，這裡的 parse() 純為加 cookies 功用
        yield response.follow(
            url = "https://www.ptt.cc/bbs/gossiping/index.html",
            cookies = {"over18":"1"},
            callback = self.parse_info
        )

    def parse_info(self, response):
        titles = response.xpath('//div[@class="title"]/a/text()').extract()
        authors = response.xpath('//div[@class="meta"]/div[@class="author"]/text()').extract()
        for info in zip(titles, authors):
            print(f"標題: {info[0]}")
            print(f"作者: {info[1]}")