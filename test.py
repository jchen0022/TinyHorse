from util import *
from main import *
sharesList = ["ibm", "qcom", "scty", "amzn", "ilmn"]

Joe = Person('Joe')
Joe.addPortfolio('Tech Stocks')
for tick in sharesList:
    Joe.buyShares(tick, 10, '11-06-2011')
for tick in sharesList:
    Joe.addToPortfolio('Tech Stocks', tick)

print(returnEarningsShare(Joe.listOfStocks()))
print(returnPE(Joe.listOfStocks()))
print(returnPercentYear(Joe.listOfStocks()))
print(returnChanges(Joe.listOfStocks()))

