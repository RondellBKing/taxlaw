from flask import Flask, render_template, request
from taxlaw import marin  # Need a generic method to call differenct scrapers
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        results = request.form  # Input data from webpage

        scraper = marin.Marin(results.get('startDate'), results.get('endDate'))
        scraper.scrape()

        return render_template('result.html', result=scraper.result_list)

if __name__ == '__main__':
    app.run(debug=True)
