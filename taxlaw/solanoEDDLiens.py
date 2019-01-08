import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import pandas as pd
import numpy as np
import pygsheets
import os

'''Working hack to upload to Sheets.  Needs work.'''

def getSolanoEDDLiens():
    '''Turns targeted search results into local CSV'''
    browser = webdriver.Chrome(executable_path='/Users/mitchellhall'
                           '/programming/chromedriver')
    time.sleep(1)
    browser.get('http://recorderonline.solanocounty.com')
    time.sleep(1)
    browser.find_element_by_id('ctl00_m_g_c6431b47_3ecb_4f66_9e13_f949e2ea5ca6_'
                            'ctl00_btnAgree').click()
    time.sleep(1)   # needs to rest before executing next click
                # *element = WebDriverWait(driver, 10).until(
                # EC.presence_of_element_located((By.ID, "originTextField")))
    browser.find_element_by_id('ctl00_m_g_53ad86ef_2077_49cd_915b_11a033357719_'
                                'ctl00_btnShowAdvanced').click()
                                # show advanced search options
    time.sleep(1)
    # browser.find_element_by_css_selector('#ctl00_m_g_53ad86ef_2077_'
    #                             '49cd_915b_11a033357719_ctl00_btnToDate').click()
    #                             # just date selector, not specific date
    #                             # date not always live (commented: 11/25)
    browser.find_element_by_css_selector('#dk_container_ctl00_m_g_53ad86ef_2077_'
                                '49cd_915b_11a033357719_ctl00_'
                                'drpFilingCode > a > span.dk_label').click()
                                # doc title span
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="dk_container_ctl00_m_g_53ad86ef_2077_'
                               '49cd_915b_11a033357719_ctl00_drpFilingCode"]'
                               '/div[1]/ul/li[722]/a').click()
                               # lien - tax lien
    time.sleep(1)
    browser.find_element_by_css_selector('#ctl00_m_g_53ad86ef_2077_49cd_915b_'
                                '11a033357719_ctl00_btnAdvancedSearch').click()
    time.sleep(1)
    browser.find_element_by_css_selector('#a_more_snm').click()
    time.sleep(1)
    browser.find_element_by_css_selector('#ul_more_snm > li:nth-child(6) > label').click()
    time.sleep(1)
    browser.find_element_by_css_selector('#dk_container_ctl00_PlaceHolderMain_'
                                'ucSearchResults_'
                                'drpResultsPerPage > a > span.arrow').click()
                                # per page drop down
    time.sleep(1)
    browser.find_element_by_css_selector('#dk_container_ctl00_PlaceHolderMain_'
                                'ucSearchResults_'
                                'drpResultsPerPage > div.dk_options > ul > '
                                'li:nth-child(5) > a').click()
                                # 100 per page
    time.sleep(1)

    html = browser.execute_script('return document.documentElement.outerHTML')

    sel_soup = BeautifulSoup(html, 'html.parser')

    liens = sel_soup.select('tbody > tr')
        # select only the search results

    allNameRegex = re.compile('\(R\)\s{2}(.*)<')
    allDateRegex = re.compile('\d*/\d*/\d*')

    allNames = allNameRegex.findall(str(liens))
    allDates = allDateRegex.findall(str(liens))

    browser.close()

    solanoDict = {'Dates':allDates, 'Names':allNames}
    df = pd.DataFrame(solanoDict)
    solanoEDDUpdateDF = df[~df.Names.str.contains(',')]  # remove all resusts that
                                                        # look like personal name
    solanoEDDUpdateDF.to_csv('/Users/mitchellhall/programming/pyprojects'
                        '/tax-liens/solano/solanoEDDUpdateCSV', index=False)


if __name__ == '__main__':
    getSolanoEDDLiens()

solanoEDDUpdateCSV = pd.read_csv('/Users/mitchellhall/programming/pyprojects'
                                '/tax-liens/solano/solanoEDDUpdateCSV')
solanoEDDUpdateDF = pd.DataFrame(solanoEDDUpdateCSV)

gc = pygsheets.authorize(client_secret='/Users/mitchellhall/programming'
                            '/pyprojects/tax-liens/client_secret.json')
sh = gc.open('Blueprint Tax Liens')
wks = sh.worksheet_by_title('Solano EDD')
sheetValues = wks.get_all_values(include_tailing_empty=False,
                                include_tailing_empty_rows=False)
solanoEDDSheetDF = pd.DataFrame(sheetValues, columns=['Dates', 'Names'])
solanoEDDSheetCSV = solanoEDDSheetDF.to_csv('/Users/mitchellhall/programming'
                                '/pyprojects/tax-liens/solano/solanoEDDSheetCSV')
newDF = pd.concat([solanoEDDUpdateDF, solanoEDDSheetDF], sort=False).drop_duplicates()

wks.clear() # potentially hazardous call?
wks.set_dataframe(newDF, (1,1))
