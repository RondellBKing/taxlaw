import scrapy
from scraper.scraper.items import LienItem

class MarinSpider(scrapy.Spider):
    name = 'marin'
    start_urls = ['https://apps.marincounty.org/RecordersIndexSearch/']

    def parse(self, response):
        self.log('stuff happened')
        item = response.url
        headers = response.headers
        yield item
        yield headers
