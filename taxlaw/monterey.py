import requests
from bs4 import BeautifulSoup
from scraper import Scraper
from lxml import html
import webbrowser


class Monterey(Scraper):

    def make_url(self):
        self.url = 'http://192.92.176.46/Montereyweb/search/DOCSEARCH284S4'
        print(self.url)

    def scrape_page(self):
        form_data = {
        'field_RecordingDateID_DOT_StartDate': self.start_date,
        'field_RecordingDateID_DOT_EndDate': self.end_date,
        'field_selfservice_documentTypes-holderInput': '023',
        'field_selfservice_documentTypes-holderValue': 'LIEN FEDERAL',
        'field_selfservice_documentTypes-holderInput': '063',
        'field_selfservice_documentTypes-holderValue': 'LIEN',
        'field_selfservice_documentTypes-holderInput': '024',
        'field_selfservice_documentTypes-holderValue': 'TAX LIEN',
        'field_selfservice_documentTypes-containsInput': 'Contains Any'
        }

        request_url = 'http://192.92.176.46/Montereyweb/filterSearchResults/DOCSEARCH284S4?searchDimension=Grantee&paths=EMPLOYMENT%20DEVELOPMENT%20DEPARTMENT%20OF%20THE%20STATE%20OF%20CALIFORNIA'
        disclaimer_url = 'http://192.92.176.46/Montereyweb/user/disclaimer'

        cookie = {
        'JSESSIONID': '780BBD13092B06D4B4C9C110CE6D7A9',
        'BNES_JSESSIONID': '7nXSsEnwemPC9Rqwtz+uzuCF9NUvbGFuTNGHZKAollhAs1RQ7M57eOo+nGcsferGg8cJSjYD8Cp+nLfyhhLYf8pwvMjKMaUNRqjT5wOS7Is=',
        'disclaimerAccepted': 'true',
        'BNES_disclaimerAccepted': 'VsqPg2ynOQhO4JURbdcLycfo2lGcccyNZTc7JptF1ahHGSqJz+YG6lC7Zwzl3eE2huXAke7PT2hGHvvxjLUUQQ=='
        }


        # requests.Session().get(disclaimer_url)
        # requests.Session().post(disclaimer_url)
        requests.Session().get(monterey.url)
        requests.Session().post(monterey.url, data=form_data, cookies=cookie)
        page = requests.Session().get(monterey.url)
        results_soup = BeautifulSoup(page.content)
        print(results_soup)
        # webbrowser.open(results_soup)
        rows = results_soup.find_all('li')
        print(rows)

if __name__ == '__main__':
    monterey = Monterey(input('Start Date(dd/mm/yyyy): '), input('End Date(dd/mm/yyyy): '))
    monterey.make_url()
    monterey.scrape_page()
