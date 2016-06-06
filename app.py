from flask import Flask, render_template, request, redirect
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/index', methods=['POST'])
def my_form_post():

    text = request.form['ticker']
    splot(text)
    return render_template('timeseries.html')
  
def splot(text):
    url1 = 'https://www.quandl.com/api/v3/datasets/WIKI/'
    url2 = text
    url3 = '/data.json?start_date=2015-05-01&end_date=2015-05-31'
    
    url = url1 + url2 + url3
    
    r = requests.get(url)
    
    data = r.json()
    data2 = data['dataset_data']['data']
    data3 = pd.DataFrame(data2,columns = data['dataset_data']['column_names'])

    from bokeh.charts import TimeSeries, show, output_file, vplot

    data = dict(
        AAPL=data3['Adj. Close'],
        Date=data3['Date']
    )

    tsline = TimeSeries(data,
        x='Date', y=['AAPL'],
        color=['AAPL'], dash=['AAPL'],
        title="Timeseries", ylabel='Stock Prices', legend=True)

    output_file("timeseries.html")

    show(vplot(tsline))
    

if __name__ == '__main__':
  app.run(port=33507)
