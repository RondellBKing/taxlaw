import scrapy
from scraper.scraper.items import LienItem
import urllib.parse

class MarinSpider(scrapy.Spider):
    name = 'marin'
    allowed_domains = ['marincounty.org']

    def start_requests(self):
       base_url = 'https://apps.marincounty.org/RecordersIndexSearch/'
               
       query = urllib.parse.urlencode({
               'Action': 'T', 
               'TDT': 'LIEN',
               'TED': '04/03/2019',
               'TSD': '03/01/2019',
               'TED': '04/03/2019',
               'XHideDisclaimer': 'True',
               })

       action_url = base_url + '?' + query
       
       urls = [
               action_url,
               ]

       for url in urls:
           yield scrapy.Request(url=action_url, callback=self.parse)

    def parse(self, response):
        self.log('stuff happened')
        item = LienItem()
        item['headers'] = response.headers
        item['body'] = response.body
        item['url'] = response.url

        return item

    table = response.css('table.i27')
    rows = table.css('tr')
    elements = rows.css('td')
    urls = elements.css('a')
