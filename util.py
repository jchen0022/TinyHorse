from yahoo_finance import *
import random, numpy, datetime, pylab

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

def returnPrice(sharesList, startTime, endTime, timeStep = 10):
    """Returns tuple of ticker names list and a dictionary
    of the price of shares in sharesList over time"""
    xTime = []
    yPrices = {}
    for time in range(startTime, endTime, timeStep+1):
        xTime.append(time)
    for time in xTime:
        for share in sharesList:
            yPrices[str(share.data_set["Symbol"])] = float(share.get_price())
    return (xTime, yPrices)
