import requests
from bs4 import BeautifulSoup
import webbrowser
from scraper import Scraper

class Marin(Scraper):
    url = 'https://apps.marincounty.org/RecordersIndexSearch?XHideDisclaimer=True' # after accepting disclaimer
    base_url = 'https://apps.marincounty.org'

    def make_url(self):
        smonth = start_date[0:2]
        sday = start_date[3:5]
        syear = start_date[6:]
        emonth = end_date[0:2]
        eday = end_date[3:5]
        eyear = end_date[6:]
        result_url = 'https://apps.marincounty.org/RecordersIndexSearch/?Action=T&TDT=TAX%20LIEN&TED={}%2F{}%2F{}&TSD={}%2F{}%2F{}'.format(emonth, eday, eyear, smonth, sday, syear)
        print(result_url)

# table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="i0")
# rows = table.findAll(lambda tag: tag.name=='tr')

    # res = requests.get(result_url)
    # res.raise_for_status()
    #
    # soup = BeautifulSoup(res.content, "html.parser")
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
