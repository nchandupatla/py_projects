import pandas_datareader as pdr
from time import sleep

def get_stock_prices(list):
    for i in list:
        res = pdr.get_quote_yahoo(i)["price"]
        print(res)

def tracker(list, sec):
    i = 1
    while i > 0:
        sleep(sec)
        get_stock_prices(list)

list = "aapl msft fb plx hd goog".split()
tracker(list, 10)