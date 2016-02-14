from yahoo_finance import *
import random, numpy, datetime, string

"""
Philosophy: percent are superior to raw changes.

"""

def getPrice(share):
    return float(share.get_price())

def getName(share):
    return str(share.data_set['symbol'])

def getMovingAvg50(share):
    return float(share.get_50day_moving_avg())

def getMovingAvg200(share):
    return float(share.get_200day_moving_avg())


def getEarningsShare(share):
    return float(share.get_earnings_share())
    
def getPE(share):
    return float(share.get_price_earnings_ratio())

def get_maxChange_year(share):
    """Returns (year high - year low) / (year low)""" 
    yearHigh = float(share.get_year_high())
    yearLow = float(share.get_year_low())
    maxChange = (yearHigh - yearLow) / (yearLow)
    return maxChange

def get_change_50day(share):
    currentPrice = getPrice(share)
    movingAvg = getMovingAvg50(share)
    return (movingAvg - currentPrice) / (currentPrice)

# Helpers =====

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

# Helpers =====


def getPriceHistory(shareList, startDate, endDate, timeStep = 1):
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
    

def get_price_date(share, date = datetime.date.today()):
    return float(share.get_historical(date, date)[0][u'Close'])



