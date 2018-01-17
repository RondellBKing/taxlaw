import urllib2
import csv
from datetime import datetime
from bs4 import BeautifulSoup


quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser") # Contains html

name = soup.find("h1", attrs={"class": "name"}).text
price = soup.find("div", attrs={"class": "price"}).text

data = []
data.append((name,price))

print name
print price


def save_to_excel(name, data):
    with open(name,'a') as csv_file:
        writer = csv.writer(csv_file)
        # The for loop
        for name, price in data:
            writer.row([name, price])

