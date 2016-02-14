from yahoo_finance import *
import random, datetime
from share_init import *
from util import *
"""
Philosophy:
1. Low price compared to 50 day moving average
2. Possesses long-term value
3. Factors in opportunity costs of ditching current possessions

"""
shareList = [tsla, qcom, ilmn, ibm, scty, aapl, goog]
def compareShares(sList = shareList):
    for share in sList:
        print str(getName(share)+":")
        print "Biggest change in year: " + str(round(get_maxChange_year(share),3))
        print "Difference from 50 day average: " + str(get_change_200day(share))


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
    
    # ==== IMPORTANT ====
    """allPurchases Structure: {tick: {dateBought: numShares}}"""

    def buyShares(self, tick, numShares, dateBought = datetime.date.today()):
        """Buys (numShares) of (tick) stock"""
        try:
            purchaseHistory = self.allPurchases[tick] # Checks if Person owns the stock
            self.allPurchases[tick].addShares(tick, numShares, dateBought)
        except KeyError:
            self.allPurchases[tick] = Purchase(tick, numShares, dateBought)
            
    # ====================

        
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
    







    
