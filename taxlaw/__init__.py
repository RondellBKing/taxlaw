from flask import Flask, render_template, request
from datetime import datetime
from taxlaw import marin  # Need a generic method to call different scrapers
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

        scraper = marin.Marin(start_date, end_date)
        scraper.scrape()

        return render_template('result.html', result=scraper.results)

if __name__ == '__main__':
    app.run(debug=True)
