from yahoo_finance import *
import random, numpy, datetime, pylab

"""
How do you instantiate a share? Use its ticker symbol.  
ibm = Share("IBM")

"""
"""
Initialize Person with name:


"""
class Person(object):
    def __init__(self, name):
        self.name = name
        self.portfolios = {} 
        self.all_stocks = {} #KEEPS TRACK OF GENERIC TYPES OF STOCK OWNED
        """
        all_stocks holds all the stock types
        format: {String tick, Stock}
        self.portfolio: a
        """
        self.history = {} #KEEPS TRACK OF STOCK PURCHASE INFORMATION
        """
        Keeps track of the stock information.
        Automatically updates when buyShares is called
        Format: {tick: {date: purchase_information}}
        """
    def addPortfolio(self, title):
        self.portfolio[title] = Portfolio(title)
    def addToPortfolio(self, title, tick):
        """Takes in a portfolio title and stock's tick and 
        adds stock into portfolio
        Stock must already be owned by Person"""
        if tick not in self.all_stocks:
            raise Exception
        stock_location = self.all_stocks[tick]
        self.portfolio[title].addStock(tick, stock_location)
    def buyShares(self, tick, num_shares, date):
        """Buys (num_shares) shares of (tick) stock. Then documents into Person.history"""
        if tick not in self.all_stocks:
            new_stock = Stock(Share(tick), tick)
            self.all_stocks[tick] = new_stock
        else:
            self.all_stock[tick].num_shares += num_shares
        self.history[stock.tick][date] = StockHistory(Share(tick), tick, num_shares, date)       #CHANGE THIS DATE NOT WORKING
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
    def __init__(self, share, tick, num_shares):
        self.stock_info = stock_info #provided by yahoo-finance module
        self.tick = tick
        self.num_shares = 0
    def getPrice(self):
        self.share.get_price()
    def getNumShares(self):
        return self.num_shares

class StockHistory(Stock):
    """For getting information on stocks previously bought"""
    def __init__(self, share, tick, num_shares, date):
        Stock.__init__(self, share, tick)
        self.price = share.getprice()
        self.date = date
        self.num_shares = num_shares
    def getPrice(self):
        """Get price of stock at the time of purchase"""
        return self.price
    def getNumShares(self):
        return self.num_shares
