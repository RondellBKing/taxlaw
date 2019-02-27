from taxlaw import Configuration
import xlsxwriter
import requests
from bs4 import BeautifulSoup
from taxlaw.scraper import Scraper
from datetime import datetime
import logging

logger = logging.getLogger('Fresno-Scraper')
logger.setLevel(logging.INFO)


class Fresno(Scraper):
    def __init__(self, start_date, end_date):
        self.start_date = datetime.strftime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strftime(end_date, "%Y-%m-%d")
        super().__init__(start_date, end_date)
        self.result_url = ""
        self.results = []

    def scrape(self):
        self.make_url()
        self.get_table()

    def make_url(self):
        url = "http://www.criis.com/cgi-bin/doc_search.cgi?COUNTY=fresno&YEARSEGMENT=current&TAB=3#"
        base_url = "http://www.criis.com"

        res = requests.get(url)
        res.raise_for_status()

        main_soup = BeautifulSoup(res.content, "html.parser")

        action_url = main_soup.find('form').get('action')
        self.result_url = "{}{}".format(base_url, action_url)

        logger.info("Form url is {}".format(self.result_url))
        print("Form url is {}".format(self.result_url))

    def get_table(self):

        # Form data
        data = {"DOC_TYPE": "026",  # Federal Tax Lien
                "doc_date_A": "08012018",
                "doc_date_B": "11012018",
                "SEARCH_TYPE": "DOCTYPE",
                "YEARSEGMENT": "current",
                "ORDER_TYPE": "Recorded Official",
                "LAST_RECORD": "1",
                "SCREENRETURN": "doc_search.cgi",
                "SCREEN_RETURN_NAME": "Recorded Document Search",
                }

        post = requests.post(self.result_url, data=data)  # Response page

        if post.status_code == 200:
            logger.info('Page Returned successfully!')
            results_soup = BeautifulSoup(post.content, "html.parser")
            self.results = results_soup.find_all('tr')[9:]  # Header data starts here
            self.results = [row.find_all('td') for row in self.results if len(row) == 13]

        else:
            logger.error('Query failed to return results -> response code {}'.format(post.status_code))
            logger.error('Page query ->:{}'.format(data))

    def write_results(self):
        for data in self.results:
            xlsxwriter.Workbook()
            logger.warning("Name:{} - Date:{}".format(data[1].string, data[5].string))


if __name__ == '__main__':
    start_dt = datetime.strptime(input('Start Date(dd/mm/yyyy): '), "%m/%d/%Y")
    end_dt = datetime.strptime(input('End Date(dd/mm/yyyy): '), "%m/%d/%Y")
    fresno = Fresno(start_dt, end_dt)
    fresno.scrape()
    for i in fresno.results:
        print(i)
