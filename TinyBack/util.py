from yahoo_finance import *
import random, numpy, datetime, pylab, string

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
        try:
            yVals.append(float(share.get_price_earnings_ratio()))
        except TypeError:
            yVals.append(0)
    return (xVals, yVals)

def returnPercentYear(sharesList):
    """Returns tuple of ticker names and (year high - year low) / (year high)"""
    xVals = []
    yVals = []
    for share in sharesList:
        xVals.append(str(share.data_set["Symbol"]))
        yearHigh = float(share.get_year_high())
        yearLow = float(share.get_year_low())
        percentChange = (yearHigh - yearLow) / (yearHigh)
        yVals.append(percentChange)
    return (xVals, yVals)

def stringToDatetime(stringDate): 
    """Converts string to datetime object with date format 'year-month-day' """
    stringList = stringDate.split('-')
    return datetime.date(int(stringList[0]), int(stringList[1]), int(stringList[2]))

def deltaToInt(timeDelta):
    """Converts datetime.timedelta object into int"""
    timeDeltaStringList = str(timeDelta).split(' ')
    return timeDeltaStringList[0]
    
def priceHistory(share, startDate, endDate, timeStep): #Helper function to sharesPriceHistory
    """Assumes dates entered in string format 'year-month-day'
    Output: list of prices"""
    timeDeltaDatetime = stringToDatetime(endDate) - stringToDatetime(startDate)
    timeDeltaInt = deltaToInt(timeDeltaDatetime)
    results = []
    for index in range(0, timeDeltaInt, timeStep):
        priceHistorical = share.get_historical(startDate, endDate)[index][u'Close']
        results.append(priceHistorical)
    return results

def sharesPriceHistory(shareList, startDate, endDate, timeStep = 1):
    """Output: (timeStep string list, dictionary[share] = price list)"""
    timeDeltaDatetime = stringToDatetime(endDate) - stringToDatetime(startDate)
    timeDeltaInt = deltaToInt(timeDeltaDatetime)
    startDatetime = stringToDatetime(startDate)
    xTime = [startDatetime]
    sharePrices = {}
    for index in range(0, timeDeltaInt, timeStep):
        startDatetime += datetime.timedelta(timeStep)
        xTime.append(str(startDatetime))
    for share in shareList:
        sharePrices[share] = priceHistory(share, startDate, endDate, timeStep)
    return (xTime, sharePrices)
    
def returnChanges(sharesList):
    """Returns tuple of ticker names list and a list of
    percent change of price of shares"""
    xVals = []
    yVals = []
    for share in sharesList:
        xVals.append(str(share.data_set["Symbol"]))
        yVals.append(float(share.get_change()))
    return (xVals, yVals)

def getPrice(share, date = datetime.date.today()):
    """Returns price of input date"""
    return float(share.get_historical(date, date)[0][u'Close'])


### ==========
### READS AND INSTANTIATES SHARES
### ==========
    
def instantiateShare(line):
    pass

