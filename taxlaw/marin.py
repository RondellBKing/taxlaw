import requests
from bs4 import BeautifulSoup
from scraper import Scraper
from lxml import html
import webbrowser


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

        for tr in list(table):
            if '>TAX LIEN<' in str(tr):
                url = tr.a.get('href')
                disclaimer = '&XHideDisclaimer=True'
                page = url + disclaimer
                print(page)
#
#         for element, tag, url, other in links_list[5:]:
#             disclaimer = '&XHideDisclaimer=True'
#             page = url + disclaimer
#             print('\n' + page + '\n')
#             # res = requests.get(page)
#             # res.raise_for_status()
#             # soup = BeautifulSoup(res.content, 'html.parser')
#             # doc_title = '//*[@id="main-content"]/div[2]/div[3]/div/div[1]/table/tbody/tr[3]/td[2]'
#             # if 'RELEASE' in soup:
#             #     print('no result')
#             # else:
#             #     webbrowser.open(page)
#
# html = html.fromstring(str(rows[2]))
# link = list(html.iterlinks())
# link_as_list = str(link[0]).split(',')
# url = actually_a_list[2][2:-1]
#
marin = Marin(input('Start Date: '), input('End Date: '))
marin.make_url()
marin.html_parse()
#
# for tr in table:
#     if '>TAX LIEN<' in str(item):
#         print(item)
#
# for item in list(rows):
#     if '>TAX LIEN<' in str(item):
#         html = html.fromstring(str(item))
#         link = list(html.iterlinks())
#         link_as_list = str(link[0]).split(',')
#         url = actually_a_list[2][2:-1]
#         print(url)
#         # html_list = html.fromstring(str(item))
#         # link = list(html_list.iterlinks())
#         # print(link[2]) # link is a list of 1 item?
#         # # print('\n' + str(item) + '\n')
#     else:
#         print('Wrong doc title')
