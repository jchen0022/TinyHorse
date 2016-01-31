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
        self.portfolios[title] = Portfolio(title)
    def listOfStocks(self): #MAKE CHANGE LATER SHOULD BE A VARIABLE
        return [stock_object.stock_info for stock_object in self.all_stocks.values()]
    def addToPortfolio(self, title, tick):
        """Takes in a portfolio title and stock's tick and 
        adds stock into portfolio
        Stock must already be owned by Person"""
        if tick not in self.all_stocks:
            print(tick)
            raise Exception
        stock_location = self.all_stocks[tick]
        self.portfolios[title].addStock(tick, stock_location)
    def buyShares(self, tick, num_shares, date):
        """Buys (num_shares) shares of (tick) stock. Then documents into Person.history"""
        if tick not in self.all_stocks:
            print(tick)
            new_stock = Stock(Share(tick), tick)
            self.all_stocks[tick] = new_stock
            self.history[tick] = {}
        else:
            self.all_stock[tick].num_shares += num_shares
        self.history[tick][date] = OriginalStock(Share(tick), tick, num_shares, date)       #CHANGE THIS DATE NOT WORKING
    def getOriginalStock(self, tick):
        """Returns dict containing all {date: OriginalStock}"""
        return self.history[tick]
    def getStock(self, tick):
        return self.all_stocks[tick]
        
class Portfolio(object):
    """Portfolio of investments containing number of investments,
    subject to analyses of individual shares"""
    def __init__(self, title):
        self.title = title
        self.stocks = {}  #TICK: STOCK LOCATED IN PERSON.ALL_STOCKS
    def addStock(self, tick, stock):
        self.stocks[tick] = stock

class Stock(object):
    """All shares of a stock"""
    def __init__(self, stock_info, tick):
        self.stock_info = stock_info #Share class provided by yahoo-finance module
        self.tick = tick
        self.num_shares = 0
    def getPrice(self):
        self.share.get_price()
    def getNumShares(self):
        return self.num_shares

class OriginalStock(Stock):
    """For getting information on stocks previously bought"""
    def __init__(self, share, tick, num_shares, date):
        Stock.__init__(self, share, tick)
        self.price = share.get_price()
        self.date = date
        self.num_shares = num_shares
    def getPrice(self):
        """Get price of stock at the time of purchase"""
        return self.price
    def getNumShares(self):
        """Get number of shares that was purchased at the time"""
        return self.num_shares
