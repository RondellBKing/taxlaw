# Base Class for the web scrapers. Web scrapers inherit this class.


class Scraper (object):

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.results = ""
        self.error = ""

    def scrape(self):
        # DO scraping things!
        print(self.start_date)
        print(self.end_date)
        self.results = 'results'

    def write_results(self):
        # Google Sheets for now - > https://developers.google.com/sheets/api/quickstart/python
        # Todo Mitch implement the solution for google sheets
        print(self.results)