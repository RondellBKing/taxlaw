from flask import Flask, render_template, request
from datetime import datetime
import importlib
from taxlaw import marin
app = Flask(__name__)


def datetime_format(value, dt_format='%Y-%m-%d'):
    return datetime.strptime(value, dt_format)

#environment.filters['datetimeformat'] = datetimeformat

# written on: {{ article.pub_date|datetimeformat }}
# publication date: {{ article.pub_date|datetimeformat('%d-%m-%Y') }}


# Landing Page
@app.route("/")
def index():

    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        results = request.form

        # Store dates in datetime object for universal use, parsing done as needed.
        start_date = datetime_format(results.get('startDate'))
        end_date = datetime_format(results.get('endDate'))

        # Determine the region to scrape based on the user input
        region = results.get('regionName')
        region_module = importlib.import_module(region, package="taxlaw")
        region_cl = getattr(region_module, region.capitalize())
        scraper = region_cl(start_date, end_date)

        scraper.scrape()

        return render_template('result.html', result=scraper.results)

if __name__ == '__main__':
    app.run(debug=True)
