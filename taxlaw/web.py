import pyperclip
from taxlaw import Configuration
import webbrowser
import xlsxwriter
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
from dateutil import parser
import logging

logger = logging.getLogger('WebScraper')
logger.setLevel(logging.INFO)


def getsite():
    pass


def getlead():
    pass


def write_results():
    pass


def validate_date(msg):
    while True:
        date = input(msg)
        if date == 'end':
            sys.exit('Closing web scaper')
        try:
            parser.parse(date)
        except Exception:
            print("Incorrect data format, should be MM-DD-YYYY")
            continue
        else:
            return date


def get_input_county(msg):
    while True:
        county = input(msg)
        if county.lower() == 'end':
            sys.exit('Closing web scaper')

            continue
        else:
            return url


#browrser = webdriver.Firefox()
#browser.get(url)
#linkElem = browser.find_element_by_link_text('Link text')
#linkElem.click() # Click link

def main():

    # url = get_input_county('Enter the county name: ')
    # date = get_input_date('Enter the starting date: ')

    url = "http://www.criis.com/cgi-bin/doc_search.cgi?COUNTY=fresno&YEARSEGMENT=current&TAB=3#"
    base_url = "http://www.criis.com"
    res = requests.get(url)
    res.raise_for_status()

    main_soup = BeautifulSoup(res.content, "html.parser")
    action_url = main_soup.find('form').get('action')
    data = {"DOC_TYPE": "026", # Federal Tax Lien
            "doc_date_A": "08012018",
            "doc_date_B": "11012018",
            "SEARCH_TYPE": "DOCTYPE",
            "YEARSEGMENT": "current",
            "ORDER_TYPE": "Recorded Official",
            "LAST_RECORD": "1",
            "SCREENRETURN": "doc_search.cgi",
            "SCREEN_RETURN_NAME": "Recorded Document Search",
            }
    form_url = "{}{}".format(base_url, action_url)
    logger.info("Form url is {}".format(form_url))
    post = requests.post(form_url, data=data)
    #webbrowser.open(post.url)  # Needed for the cookie I think

    if post.status_code == 200:
        logger.info('Page Returned successfully!')
        results_soup = BeautifulSoup(post.content)
    else:
        logger.error('Query failed to return results -> response code {}'.format(post.status_code))
        logger.error('Page query ->:{}'.format(data))
        return

    rows = results_soup.find_all('tr')
    #print(results_soup)
    for data in rows[9:]:
        if len(data) == 13:
            cells = data.find_all('td')
            xlsxwriter.Workbook()
            logger.warning("Name:{} - Date:{}".format(cells[1].string, cells[5].string))

if __name__ == '__main__':
    main()


print('hi')