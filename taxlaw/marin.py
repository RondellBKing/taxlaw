import requests
from bs4 import BeautifulSoup
from scraper import Scraper
from lxml import html
import webbrowser
import pygsheets


class Marin(Scraper):

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

        url_list = []
        for tr in list(table):
            if '>TAX LIEN<' in str(tr):
                url = tr.a.get('href')
                disclaimer = '&XHideDisclaimer=True'
                page = url + disclaimer
                url_list.append(page)

        self.result_list = []
        for link in url_list:
            link_result = []
            res = requests.get(link)
            res.raise_for_status()
            soup = BeautifulSoup(res.content, 'html.parser')
            table = soup.find('table')
            for row in table.findAll('tr'):
                text = row.text.replace('class=\"i19\"', '')
                link_result.append(text)
            self.result_list.append(link_result)

    def write(self):
            gc = pygsheets.authorize(client_secret='/Users/mitchellhall/programming/pyprojects/taxlaw/taxlaw/credentials.json')
            sh = gc.open('Lien Lead Generation')
            wks = sh.worksheet_by_title('Sheet1')
            wks.update_values(crange='A1', values=self.result_list)


if __name__ == '__main__':
    marin = Marin(input('Start Date(dd/mm/yyyy): '), input('End Date(dd/mm/yyyy): '))
    marin.make_url()
    marin.html_parse()
