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
    def addPortfolio(self, portfolio):
        self.portfolio.append(portfolio)
        
class Portfolio(object):
    """Portfolio of investments containing number of investments,
    subject to analyses of individual shares"""
    def __init__(self, title):
        self.title = title
        self.shares = [];
    def addShare(self, share):
        self.shares.append(share)
