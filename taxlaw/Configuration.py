"""
This file stores the specific details for each site.
Required fields must be populated.
Developer can add additional fields based on the complexity of the site but all sites will likely have the required
fields.

The keyword of the main dict, is the county name (user input).
Required Fields:
    base_url - not a functional url but the base page, useful when executing form actions
    url - landing page for the web scraper, this should probably be the starting point in terms of web mining
    form_data - fields passed to the form action that will get you the results


"""


scraper_input = {
    "fresno": {'base_url': "http://www.criis.com",
               'url': "http://www.criis.com/cgi-bin/doc_search.cgi?COUNTY=fresno&YEARSEGMENT=current&TAB=3#",
               'form_data':  {"DOC_TYPE": "026",  # Federal Tax Lien
                         "doc_date_A": "08012018",  # Todo this will be input from the user
                         "doc_date_B": "11012018",  # Todo this will be input from the user
                          "SEARCH_TYPE": "DOCTYPE",
                          "YEARSEGMENT": "current",
                          "ORDER_TYPE": "Recorded Official",
                          "LAST_RECORD": "1",
                          "SCREENRETURN": "doc_search.cgi",
                           "SCREEN_RETURN_NAME": "Recorded Document Search"
                         }
               }
}
