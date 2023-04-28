from flask import Flask, render_template, request
import python_stock_functions
from python_stock_functions import find_FV, find_NPER, find_PMT, find_PV, find_RATE, top_10, bottom_10, company_information, compare
import requests
from api_keys import stock_ticker_api, finnhub_key
# from python_stock_functions import
# Add to the imports when the functions are done

###
"""
Make sure to Hide all API keys
"""
###

app = Flask(__name__)

@app.route('/') #Re format the Screen so it looks presentable
def index():
    return render_template('index.html')

@app.route('/button1') #This is the Financial Calculator
def button1():
    return render_template('button1.html')

@app.post('/submit')
def find_solution():
    """"""
    answer = 'None'
    Found_Answer = 'None'
    if request.form['NPER'] == '?':
        RATE = float(request.form['RATE'])
        PV = float(request.form['PV'])
        PMT = float(request.form['PMT'])
        FV = float(request.form['FV'])
        answer = find_NPER(RATE, PV, PMT, FV)
        Found_Answer = 'NPER'
    elif request.form['RATE'] == '?':
        NPER = float(request.form['NPER'])
        PV = float(request.form['PV'])
        PMT = float(request.form['PMT'])
        FV = float(request.form['FV'])
        answer = find_RATE(NPER, PV, PMT, FV)
        Found_Answer = 'RATE'
    elif request.form['PV'] == '?':
        NPER = float(request.form['NPER'])
        RATE = float(request.form['RATE'])
        PMT = float(request.form['PMT'])
        FV = float(request.form['FV'])
        answer = find_PV(NPER, RATE, PMT, FV)
        Found_Answer = 'PV'
    elif request.form['PMT'] == '?':
        NPER = float(request.form['NPER'])
        RATE = float(request.form['RATE'])
        PV = float(request.form['PV'])
        FV = float(request.form['FV'])
        answer = find_PMT(NPER, RATE, PV, FV)
        Found_Answer = 'PMT'
    elif request.form['FV'] == '?':
        NPER = float(request.form['NPER'])
        RATE = float(request.form['RATE'])
        PV = float(request.form['PV'])
        PMT = float(request.form['PMT'])
        answer = find_FV(NPER, RATE, PV, PMT)
        Found_Answer = 'FV'
    else:
        NPER = float(request.form['NPER'])
        RATE = float(request.form['RATE'])
        PV = float(request.form['PV'])
        PMT = float(request.form['PMT'])
        FV = float(request.form['FV'])
    return render_template('Fin_Cal_answer.html', answer = answer, Found_Answer = Found_Answer) #, NPER=NPER, RATE=RATE, PV=PV, PMT=PMT, FV=FV )


@app.route('/button2') #This Finds the best and wrost performing stock of the day
def button2():
    return render_template('button2.html')

@app.route('/best')
def best():
    top_10()
    return render_template('button2.html')

@app.route('/worst')
def worst():
    bottom_10()
    return render_template('button2.html')


"""Stock Ticker was attempted multiple differnet ways and was not able to be completed sadly"""
# @app.route('/button3') #This is the Stock Ticker 
# def button3():
#     api_key_ticker = stock_ticker_api()
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SPX&interval=1min&apikey={api_key_ticker}'
#     response = requests.get(url)
#     data = response.json()
#     ticker = data['Time Series (1min)']
#     return render_template('button3.html', ticker=ticker)

@app.route('/button4') #This is the simplified mortgage calculator
def button4():
    return render_template('button4.html')

@app.post('/mortgage')
def find_mortgage_rate_or_payment():
    answer = "None"
    Found_Answer = 'None'
    if request.form['RATE'] == '?':
        NPER = 12 * float(request.form['NPER'])
        PV = float(request.form['PV'])
        PMT = float(request.form['PMT'])
        answer = find_RATE(NPER, PV, PMT, 0)
        Found_Answer = 'Monthly Rate Required'
    elif request.form['PMT'] == '?':
        NPER = 12 * float(request.form['NPER'])
        RATE = float(request.form['RATE']) / 12
        PV = float(request.form['PV'])
        answer = find_PMT(NPER, RATE, PV, 0)
        Found_Answer = 'Payment Required'
    else:
        # NPER = float(request.form['NPER'])
        # RATE = float(request.form['RATE'])
        # PV = float(request.form['PV'])
        # PMT = float(request.form['PMT'])
        # FV = float(request.form['FV'])
        None
    return render_template('mortgage_ans.html', answer = answer, Found_Answer = Found_Answer)


@app.route('/button5') #This is the Stock Ticker Analysis
def button5():
    return render_template('button5.html')

@app.post('/Ticker')
def Ticker():
    Ticker = request.form['Ticker']
    Name, Sector, Industry, CurrentPrice, Recommendation, Business_Summary = company_information(Ticker)
    return render_template('Ticker.html', Name=Name, Sector=Sector, Industry=Industry, CurrentPrice=CurrentPrice, Recommendation=Recommendation, Business_Summary=Business_Summary)

@app.route('/button6') # This is the two stock comparative analysis
def button6():
    return render_template('button6.html')

@app.post('/Compare')
def comparison():
    Ticker1=request.form['Ticker1']
    Ticker2=request.form['Ticker2']
    currentPrice1, ebitdaMargins1, enterpriseValue1, forwardEps1, forwardPE1, pricetoBook1, revenuePerShare1 = compare(Ticker1)
    currentPrice2, ebitdaMargins2, enterpriseValue2, forwardEps2, forwardPE2, pricetoBook2, revenuePerShare2 = compare(Ticker2)
    return render_template('compare.html',currentPrice1=currentPrice1, currentPrice2=currentPrice2, ebitdaMargins1=ebitdaMargins1, ebitdaMargins2=ebitdaMargins2, enterpriseValue1=enterpriseValue1, enterpriseValue2=enterpriseValue2, forwardEps1=forwardEps1, forwardEps2=forwardEps2, forwardPE1=forwardPE1, forwardPE2=forwardPE2, pricetoBook1=pricetoBook1, pricetoBook2=pricetoBook2, revenuePerShare1=revenuePerShare1, revenuePerShare2=revenuePerShare2, Ticker1=Ticker1, Ticker2=Ticker2)

if __name__=='__main__':
    app.run(debug=True)
