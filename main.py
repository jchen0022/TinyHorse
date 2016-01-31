from yahoo_finance import *
import random, numpy, datetime, pylab

"""
How do you instantiate a share? Use its ticker symbol.  
ibm = Share("IBM")

"""
class Person(object):
    def __init__(self, name):
        self.name = name
        self.portfolios = [] 
        all_stocks = {}           #KEEPS TRACK OF TYPES OF STOCK OWNED
        all_info = {}
    def addPortfolio(self, portfolio):
        self.portfolio.append(portfolio)
    def addToPortfolio(self, stock, portfolio):
        self.portfolio.addStock(stock)
    def buyShares(self, ticks, num, date):
        """add to date and price"""
        if tick not in self.all_stocks:
            newStock = Stock(Share(tick), tick)
            self.all_stocks[tick] = newStock
        else:
            self.all_stock[tick].shares += num
        all_info[stock.tick][date] = StockHistory(Share(tick), tick, num, date)       #CHANGE THIS DATE NOT WORKING
    def getDatePrice(self, share):
        """Returns dict containing all {date: StockHistory}"""
        return self.all_info[share.tick]
        
class Portfolio(object):
    """Portfolio of investments containing number of investments,
    subject to analyses of individual shares"""
    def __init__(self, title):
        self.title = title
        self.stock = [];
    def addStock(self, stock):
        self.stock.append(stock)

class Stock(object):
    """All shares of a stock"""
    def __init__(self, share, tick):
        self.stock_info = stock_info #provided by yahoo-finance module
        self.tick = tick
        self.shares = 1
    def getPrice(self):
        self.share.get_price()

class StockHistory(Stock):
    """For getting information on stocks previously bought"""
    def __init__(self, share, tick, num, date):
        Stock.__init__(self, share, tick)
        self.date = date
        self.num = num
