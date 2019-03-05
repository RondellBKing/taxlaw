import requests
from bs4 import BeautifulSoup
from scraper import Scraper
from lxml import html
from solano_data import url, cookies, headers, data
from datetime import datetime


class Solano(Scraper):

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)

    def scrape(self):
        page = requests.post(url, headers=headers, cookies=cookies, data=data)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == "searchres_grid")

        print(table)

if __name__ == '__main__':
    start_dt = datetime.strptime(input('Start Date(dd/mm/yyyy): '), "%d/%m/%Y")
    end_dt = datetime.strptime(input('End Date(dd/mm/yyyy): '), "%d/%m/%Y")
    solano = Solano(start_dt, end_dt)
    solano.scrape()
