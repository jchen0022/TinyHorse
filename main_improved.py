from yahoo_finance import *
import random, numpy, datetime, pylab

class Person(object):
    def __init__(self, name):
        self.name = name
        self.portfolios = {} 
        self.allPurchases = {}
        
    def addPortfolio(self, title):
        """Add a portfolio object to instantiated Person"""
        self.portfolios[title] = Portfolio(title)
        
    def showPortfolio(self, title):
        return self.portfolios[title]
    

# IMPORTANT
# ===========
"""allPurchases Structure: {tick: {dateBought: numShares}}"""

    def buyShares(self, tick, numShares, dateBought = datetime.date.today()):
        """Buys (numShares) of (tick) stock"""
        try:
            purchaseHistory = self.allPurchases[tick] # Checks if Person owns the stock
            self.allPurchases[tick].addShares(tick, numShares, dateBought)
        except KeyError:
            self.allPurchases[tick] = Purchase(tick, numShares, dateBought)

        
# END =======
        
class Portfolio(object):
    """Portfolio of investments containing number of investments,
    subject to analyses of individual shares"""
    def __init__(self, title):
        self.title = title
        self.shares = {} # Share dictionary to keep track 
    def trackShare(self, tick):
        self.shares[tick] = self.allPurchases[tick].getTotalSharesBought() # Get current number of shares to keep track 

   
class Purchase(object):
    def __init__(self, tick, numShares, dateBought):
        """Should instantiate only once per tick.
        This role is left to Person.buyShares()"""
        self.shareReference = Share(tick)
        self.dateBought = dateBought
        self.purchases = {}
        self.purchases[dateBought] = numShares
        
    def addShares(self, sharesBought, dateBought):
        try:
            alreadyBoughtToday = self.purchases[dateBought]
            self.purchases[dateBought] += sharesBought
        except KeyError:
            self.purchases[dateBought] = sharesBought
        
    def getTotalSharesBought(self):
        total = 0
        for date in purchases:
            total += purchases[date]
        return total
    







    
