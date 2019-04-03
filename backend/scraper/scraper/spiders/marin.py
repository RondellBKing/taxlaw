import scrapy
from scraper.scraper.items import LienItem

class MarinSpider(scrapy.Spider):
    name = 'marin'

    def start_requests(self):
       urls = [
               'https://apps.marincounty.org/RecordersIndexSearch/',
               ]
       for url in urls:
           yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log('stuff happened')
        item = LienItem()
        item['headers'] = response.headers
        item['body'] = response.body
        item['url'] = response.url

        return item
