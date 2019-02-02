import requests
from bs4 import BeautifulSoup
from scraper import Scraper


class Marin(Scraper):
    url = 'https://apps.marincounty.org/RecordersIndexSearch?XHideDisclaimer=True' # after accepting disclaimer
    base_url = 'https://apps.marincounty.org'

    def make_url(self):
        smonth = self.start_date[0:2]
        sday = self.start_date[3:5]
        syear = self.start_date[6:]
        emonth = self.end_date[0:2]
        eday = self.end_date[3:5]
        eyear = self.end_date[6:]
        self.result_url = 'https://apps.marincounty.org/RecordersIndexSearch/?Action=N&GCO=1&GCPR=100&NDT=&NED={}%2F{}%2F{}&NFN=&NLN=EMPLOYMENT%20DEVELOPMENT%20DEPARTMENT&NMI=&NSD={}%2F{}%2F{}&XHideDisclaimer=True'.format(emonth, eday, eyear, smonth, sday, syear)
        print('\n' + 'Url being parsed: ' + self.result_url + '\n')

    def html_parse(self):
        res = requests.get(self.result_url)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, "html.parser")
        table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="i0")
        rows = table.findAll(lambda tag: tag.name=='tr')
        for row in rows[1:]:
            print(str(row) + '\n\n')

marin = Marin(input('Start Date: '), input('End Date: '))
marin.make_url()
marin.html_parse()
