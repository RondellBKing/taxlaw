#! python3
import pyperclip
from taxlaw import Configuration
import webbrowser
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
from dateutil import parser


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

    url = get_input_county('Enter the county name: ')
    date = get_input_date('Enter the starting date: ')
    #webbrowser.open(url)  # If you need to open pages

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.content, "html.parser")
    action_url = soup.find('form').get('action')
    data = {"DOC_TYPE": "TAX LIENS (FED)",
            "doc_date_A": "08/01/18",
            "doc_date_B": "11/01/18"
            }

    url += url + action_url
    requests.post(url, data=data)
    #print(soup)
if __name__ == '__main__':
    main()
