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
               'GCPR': '100',
               'TDT': 'LIEN',
               'TED': '04/03/2019',
               'TSD': '01/01/2019',
               'XHideDisclaimer': 'True',
               })

       action_url = base_url + '?' + query
       
       urls = [
               action_url,
               ]

       for url in urls:
           yield scrapy.Request(url=action_url, callback=self.parse)

    def parse(self, response):
        links = response.css('table.i27 tr td a::attr(href)').getall()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_attr)

    def parse_attr(self, response):
        self.log('stuff happened')
        item = LienItem()
        table = response.css('table.i18')
        item['recording_date'] = table.css('tr td.i21::text')[0].get()
        item['doc_title'] = table.css('tr td.i21::text')[1].get()
        item['involved'] = table.css('tr td.i21::text')[2:].getall()

            #results = table.css('tr td.i21::text').getall()
#        yield{
#                item['recording_date'] = table.css('tr td.i21::text')[0].get()
#                item['doc_title'] = table.css('tr td.i21::text')[1].get()
#                item['involved'] = table.css('tr td.i21::text')[2:].getall()
#                }
#
        yield item

#links = response.css('table.i27 tr td a::attr(href)').getall()
#disclaimer = '&XHideDisclaimer=True'
