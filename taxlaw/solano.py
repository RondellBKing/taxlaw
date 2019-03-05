import requests
from bs4 import BeautifulSoup
from scraper import Scraper
from lxml import html


class Solano(Scraper):

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)

    def scrape(self):
        self.url = 'http://recorderonline.solanocounty.com/Search/Pages/SearchResults.aspx'
        res = requests.get(self.url)
        res.raise_for_status()

        main_soup = BeautifulSoup(res.content, "html.parser")
        action_url = main_soup.find('form').get('action')
        print(action_url)
        data = {
            'ctl00$PlaceHolderMain$ucSearchInput$txtDocumentDateFrom': '1/1/2019',
            'ctl00$PlaceHolderMain$ucSearchInput$txtDocumentDateTo': '2/28/2019',
            'ctl00$PlaceHolderMain$ucSearchInput$drpFilingCode': '23',
            'ctl00$PlaceHolderMain$ucSearchInput$hdnIsAdvanceSearchResult': 'Advance',
            'ctl00$PlaceHolderMain$ucSearchResults$drpResultsPerPage': '100'
            }


import webbrowser
import requests
from bs4 import BeautifulSoup

url = 'http://recorderonline.solanocounty.com/Search/Pages/SearchResults.aspx'

data = {
    'ctl00$PlaceHolderMain$ucSearchInput$txtDocumentDateFrom': '1/1/2019',
    'ctl00$PlaceHolderMain$ucSearchInput$txtDocumentDateTo': '2/28/2019',
    'ctl00$PlaceHolderMain$ucSearchInput$drpFilingCode': '23',
    'ctl00$PlaceHolderMain$ucSearchInput$hdnIsAdvanceSearchResult': 'Advance',
    'ctl00$PlaceHolderMain$ucSearchResults$drpResultsPerPage': '100'
    }

import pprint
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint()

requests.Session().get(url)
requests.Session().post(url, data)
page = requests.Session().get(url)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == "searchres_grid")
