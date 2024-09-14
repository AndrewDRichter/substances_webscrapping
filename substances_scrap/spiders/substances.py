import scrapy


class SubstancesSpider(scrapy.Spider):
    name = "substances"
    allowed_domains = ["ilv.ifa.dguv.de"]
    start_urls = ["https://ilv.ifa.dguv.de/substances"]

    def parse(self, response):
        pass