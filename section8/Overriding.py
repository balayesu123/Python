#Example:

class Bank:
    def rateOfInterest(self):
        return 0

class XBank(Bank):
    def rateOfInterest(self):
        return 10

class YBank(Bank):
    def rateOfInterest(self):
        return 12

objx = XBank()
print(objx.rateOfInterest())   # 10

objy = YBank()
print(objy.rateOfInterest())   # 12