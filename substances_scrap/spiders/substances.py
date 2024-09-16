from typing import Iterable
from scrapy import Spider, Request


class SubstancesSpider(Spider):
    name = "substances"
    # allowed_domains = ["ilv.ifa.dguv.de"]
    # start_urls = ["https://ilv.ifa.dguv.de/substances"]

    def start_requests(self):
        url = "https://ilv-api.ifa.dguv.de/api/substance"
        # payload = "searchValue=&pageNr=0&pageSize=24"
        payload = ""
        headers = { "Content-Type": "application/json", "Referer": "https://ilv.ifa.dguv.de/"}
        yield Request(url=url, method="GET", body=payload, headers=headers, callback=self.parse)
        # yield Request(url=url, method="GET", callback=self.parse)

    def parse(self, response):
        data = response.json()
        print(".......")
        print(data)
        print(".......")
        # for substance in data["content"]:
        #     id = substance["id"]
        #     name = substance["name"]
        #     cas_number = substance["casNrs"]
        #     yield {
        #         "id": id,
        #         "substance": name,
        #         "casNum": cas_number,
        #     }