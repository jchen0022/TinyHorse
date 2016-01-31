from util import *
from main import *
sharesList = ["ibm", "qcom", "scty", "amzn", "ilmn"]

Joe = Person('Joe')
Joe.addPortfolio('Portfolio1')
for tick in sharesList:
    Joe.buyShares(tick, 10, 'date')
for tick in sharesList:
    Joe.addToPortfolio('Portfolio1', tick)

print(returnEarningShares(Joe.listOfShares()))
print(returnPE(Joe.listOfShares()))
print(returnPercentYear(Joe.listOfShares()))
print(returnChanges(Joe.listOfShares()))
