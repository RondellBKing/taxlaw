from flask import Flask, render_template, request
from datetime import datetime
from taxlaw import marin  # Need a generic method to call different scrapers
app = Flask(__name__)


def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

#environment.filters['datetimeformat'] = datetimeformat

# written on: {{ article.pub_date|datetimeformat }}
# publication date: {{ article.pub_date|datetimeformat('%d-%m-%Y') }}

@app.route("/")
def index():

    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        results = request.form  # Input data from webpage

        start_date = datetime.strptime(results.get('startDate'), '%Y-%m-%d')
        end_date = datetime.strptime(results.get('endDate'), '%Y-%m-%d')

        scraper = marin.Marin(start_date, end_date)
        scraper.scrape()

        return render_template('result.html', result=scraper.results)

if __name__ == '__main__':
    app.run(debug=True)
