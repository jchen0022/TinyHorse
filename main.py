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
        self.all_stocks = {} #KEEPS TRACK OF GENERIC TYPES OF STOCK OWNED
        self.history = {} #KEEPS TRACK OF STOCK PURCHASE INFORMATION
    def addPortfolio(self, title):
        self.portfolio.append(Portfolio(title))
    def addToPortfolio(self, portfolio, tick):
        if tick not in self.all_stocks:
            raise Exception
        stock_location = self.all_stocks[tick]
        self.portfolio.addStock(tick, stock_location)
    def buyShares(self, ticks, num, date):
        """add to date and price"""
        if tick not in self.all_stocks:
            newStock = Stock(Share(tick), tick)
            self.all_stocks[tick] = newStock
        else:
            self.all_stock[tick].numShares += num
        self.history[stock.tick][date] = StockHistory(Share(tick), tick, num, date)       #CHANGE THIS DATE NOT WORKING
    def getDatePrice(self, share):
        """Returns dict containing all {date: StockHistory}"""
        return self.history[share.tick]
        
class Portfolio(object):
    """Portfolio of investments containing number of investments,
    subject to analyses of individual shares"""
    def __init__(self, title):
        self.title = title
        self.stocks = {}  #TICK: STOCK LOCATED IN PERSON.ALL_STOCKS
    def addStock(self, tick, stock):
        self.stock[tick] = stock

class Stock(object):
    """All shares of a stock"""
    def __init__(self, share, tick, num):
        self.stock_info = stock_info #provided by yahoo-finance module
        self.tick = tick
        self.numShares = 0
    def getPrice(self):
        self.share.get_price()

class StockHistory(Stock):
    """For getting information on stocks previously bought"""
    def __init__(self, share, tick, num, date):
        Stock.__init__(self, share, tick)
        self.date = date
        self.num = num
