import urllib.request as urllib2
import csv
from datetime import datetime
from bs4 import BeautifulSoup


#quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
quote_page = 'http://rechart1.acgov.org/docdetail.asp?id=jAxNQ%3D%3DjV%03%13M%215b1%21k%217DAwMR%21%21tzI2O&ms=0&cabinet=opr&pg=&id2=TIvNwr%21E%21%03%0FMHqmbIqRYDE3%215FUBi8yM'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser") # Contains html

soup.get()
td_tags = soup.find_all('td')
td_tags = list(td_tags)

#Loop through
tag = td_tags[39]
tag.get_text('href')
tag.get()



print(td_tags)

#print(soup.prettify())


# name = soup.find("h1", attrs={"class": "name"}).text
# price = soup.find("div", attrs={"class": "price"}).text
#
# data = []
# data.append((name,price))

