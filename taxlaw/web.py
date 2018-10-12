#! python3
import pyperclip
import webbrowser
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#browrser = webdriver.Firefox()
#browser.get(url)
#linkElem = browser.find_element_by_link_text('Link text')
#linkElem.click() # Click link
url = pyperclip.paste() # Takes information from clip board
# webrowser.open() # If you need to open pages
print(url)

res= requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(url)
#soup.select(#)


def getsite():
    pass

def getlead():
    pass

def write_results():
    pass