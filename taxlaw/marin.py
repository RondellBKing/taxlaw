import requests
from bs4 import BeautifulSoup
import webbrowser
from scraper import Scraper

class Marin(Scraper):
    url = 'https://apps.marincounty.org/RecordersIndexSearch?XHideDisclaimer=True' # after accepting disclaimer
    base_url = 'https://apps.marincounty.org'

    def urls(url, base_url):
        self.url = url
        self.base_url = base_url

    sdate = input('month/day/year: ')
    edate = input('month/day/year: ')

    smonth = sdate[0:2]
    sday = sdate[3:5]
    syear = sdate[6:]
    emonth = edate[0:2]
    eday = edate[3:5]
    eyear = edate[6:]
    result_url = 'https://apps.marincounty.org/RecordersIndexSearch/?Action=T&TDT=TAX%20LIEN&TED={}%2F{}%2F{}&TSD={}%2F{}%2F{}'.format(emonth, eday, eyear, smonth, sday, syear)


# table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="i0")
# rows = table.findAll(lambda tag: tag.name=='tr')

    res = requests.get(result_url)
    res.raise_for_status()

    soup = BeautifulSoup(res.content, "html.parser")
# action_url = soup.find('form', id="T").get('action')
# data = {"TDT" : "Tax Lien", # doc title
#         "TSD" : "08012018",
#         "TED" : "12312018",
#         }
# form_url = "{}{}".format(base_url, action_url)
# print("Form url is {}".format(form_url))
# post = requests.post(form_url, data=data) # wrong format?  need to finish data?
# # webbrowser.open(post.url)
# print(BeautifulSoup(post.content))
