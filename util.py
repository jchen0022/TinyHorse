from yahoo_finance import *
import random, numpy, datetime, pylab

### Be ready to change str(share.data_set["Symbol"]) in case you want to
### have the first values as objects. Consider pylab in mind


def returnEarningsShare(sharesList):
    """Returns tuple of ticker names and their
    earnings per share"""
    xVals = []
    yVals = []
    for share in sharesList:
        xVals.append(str(share.data_set["Symbol"]))
        yVals.append(float(share.get_earnings_share()))
    return (xVals, yVals)

def returnPE(sharesList):
    """Returns tuple of ticker names and their PE ratios"""
    xVals = []
    yVals = []
    for share in sharesList:
        xVals.append(str(share.data_set["Symbol"]))
        yVals.append(float(share.get_price_earnings_ratio()))
    return (xVals, yVals)

def returnPercentYear(sharesList):
    """Returns tuple of ticker names and (year high - year low) / (year high)"""
    xVals = []
    yVals = []
    for share in sharesList:
        xVals.append(str(share.data_set["Symbol"]))
        yearHigh = share.get_year_high()
        yearLow = share.get_year_low()
        percentChange = float((yearHigh - yearLow)/(yearHigh))
        yVals.append(percentChange)
    return (xVals, yVals)

def stringToDatetime(stringDate): 
    """Creates datetime instance from string format 'year-month-day' """
    stringList = stringDate.split('-')
    return datetime.date(int(stringList[0]), int(stringList[1]), int(stringList[2]))

def deltaToInt(timeDelta):
    """Converts datetime.timedelta object into int"""
    timeDeltaStringList = str(timeDelta).split(' ')
    return timeDeltaStringList[0]
    
def priceHistory(share, startDate, endDate, timeStep): #Helper function to allPriceHistory
    """Assumes dates entered in string format 'year-month-day'
    Returns list of prices"""
    timeDeltaDatetime = stringToDatetime(endDate) - stringToDatetime(startDate)
    timeDeltaInt = deltaToInt(timeDeltaDatetime)
    results = []
    for index in range(0, timeDeltaInt, timeStep+1):
        priceHistorical = share.get_historical(startDate, endDate)[index][u'Close']
        results.append(priceHistorical)

def allPriceHistory(shareList, startDate, endDate, timeStep):
    """Returns tuple of timeSteps list and dictionary[share] and """
    
def returnPrices(sharesList, startDate, endDate):
    """Returns tuple of ticker names list and a dictionary
    of the price of shares in sharesList over time"""
    
    
def returnChanges(sharesList):
    """Returns tuple of ticker names list and a list of
    percent change of price of shares"""
    xVals = []
    yVals = []
    for share in sharesList:
        xVals.append(str(share.data_set["Symbol"]))
        yVals.append(float(share.get_earnings_share()))
    return (xVals, yVals)




