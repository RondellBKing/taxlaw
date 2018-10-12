import urllib.request as urllib2

import re
# import csv
# from datetime import datetime
from bs4 import BeautifulSoup
from mechanize import Browser


def submit_form(brw, input_name, value):
    brw[input_name] = value
    return brw.submit(name="btnLogin")


def get_page_info(site):
    url = site.get("url")
    br = Browser()
    br.set_handle_robots(False)
    br.open(url)

    if site.get("login"):
        #  Todo Make a generic login function based on site
        br.select_form(id="LOGIN")
        submit_form(br, "USERID", site.get("user_id"))

    return br


def main():
    url =
    browser = get_page_info(site)
    browser.select_form(id="quickSearchFormN")
    browser["searchTerm"] = "Craig Building Systems"
    response = browser.submit()

if __name__ == '__main__':
   main()



