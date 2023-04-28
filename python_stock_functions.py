###
""" 
This is all of the Python Functions that I will be using and testing for the project
"""
###
import math
from api_keys import stock_ticker_api, finnhub_key
import requests
import yfinance as yf
import pprint

def find_NPER(RATE, PV, PMT, FV=0):
    """
    This funntion finds the amount of periods when given RATE, PV, PMT, and FV
    """
    PV = -PV
    if RATE == 0:
        return -(PV+FV) / PMT
    else:
        return math.log((PMT-FV*RATE) / (PMT+PV*RATE), 1+RATE)


def find_RATE(NPER, PV, PMT, FV):
    """
    This function finds the rate when given NPER, PV, PMT, and FV
    """
    import numpy_financial as npf
    RATE = npf.rate(nper=NPER, pv=-PV, pmt=PMT, fv=FV)
    return f'{RATE:%}'


def find_PV(NPER, RATE, PMT, FV=0):
    """
    This fucntion finds the present value when given NPER, RATE, PMT, and FV
    """
    PV = PMT*((1-(1+RATE)**(-NPER))/RATE)
    PV += FV / (1+RATE)**NPER
    return PV


def find_PMT(NPER, RATE, PV, FV=0):
    """
    This function finds the payment when given NPER, RATE, PV, and FV
    """
    PV = -PV
    if RATE == 0:
        return -(PV+FV) / NPER
    else:
        return -(RATE * (FV+PV*(RATE+1)**NPER) / ((RATE+1)**NPER - 1))


def find_FV(NPER=0, RATE=0, PV=0, PMT=0):
    """
    This fucntion finds future/face value when given NPER, RATE, PV, and PMT
    """
    PV=-PV
    FV = PV*(1 + RATE/100.00) ** NPER + PMT * \
        ((1+RATE/100.00)**NPER-1) * (1+RATE/100.00) ** -1
    return FV


import webbrowser
APIKEY_finnhub = finnhub_key()
def top_10(): #This was orignally supposed to be an api of data but it wouldn't work, same with the worst performing stocks data
    """ This function opens the yahoo finance web page of the best performing stocks of the day """
    url = f"https://finance.yahoo.com/gainers/"
    webbrowser.open(url)
    # response = requests.get(url)
    # data = response.json()
    # top_10 = []
    # for stock in data:
    #     symbol = stock['symbol']
    #     name = stock['description']
    #     change_percent = stock['changePercent']
    #     top_10.append({'symbol': symbol, 'name':name, 'change_percent': change_percent})

    # return top_10

def bottom_10():
    """ This function opens the yahoo finance web page of the worst performing stocks of the day """
    url = f"https://finance.yahoo.com/losers/"
    webbrowser.open(url)
    # response = requests.get(url)
    # data = response.json()
    # bottom_10 = data[:10]

    # return bottom_10

def company_information(Ticker):
    """This function takes a stock's ticker and then gives back information about the company"""
    Ticker = yf.Ticker(Ticker)
    Name = Ticker.info['longName']
    Sector = Ticker.info['sector']
    Industry = Ticker.info['industry']
    CurrentPrice = Ticker.info['currentPrice']
    Recommendation = Ticker.info['recommendationKey']
    Business_Summary = Ticker.info['longBusinessSummary']
    return Name, Sector, Industry, CurrentPrice, Recommendation, Business_Summary

def compare(Ticker):
    """This function gives the values from the API that are needed for the comparison"""
    Ticker = yf.Ticker(Ticker)
    currentPrice = Ticker.info['currentPrice']
    ebitdaMargins = Ticker.info['ebitdaMargins']
    enterpriseValue = Ticker.info['enterpriseValue']
    forwardEps = Ticker.info['forwardEps']
    forwardPE = Ticker.info['forwardPE']
    priceToBook = Ticker.info['priceToBook']
    revenuePerShare = Ticker.info['revenuePerShare']
    return currentPrice, ebitdaMargins, enterpriseValue, forwardEps, forwardPE, priceToBook, revenuePerShare



def main():
    print()
    # print(find_NPER(.05, 1000, 50, 900)) #Test all of these with excel or calculator
    # print(find_RATE(10, 1000, 50, 0))
    # print(find_PV(10, .05, 50, 0))
    # print(find_PMT(10, .05, 1000, 0))
    # print(find_FV(10, .05, 100, 50))
    # print(top_10())
    # print(bottom_10())
    # print(company_information('MSFT'))



if __name__ == '__main__':
    main()
