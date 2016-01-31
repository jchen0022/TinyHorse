from util import *
from main import *
sharesList = ["ibm", "qcom", "scty", "amzn", "ilmn"]

Person('Joe');
Person.addPortfolio('Portfolio1')
for tick in sharesList:
    Person.addToPortfolio(tick)

print(returnEarningShares(Person.listOfShares()))
print(returnPE(Person.listOfShares()))
print(returnPercentYear(Person.listOfShares()))
print(returnChanges(Person.listOfShares()))
