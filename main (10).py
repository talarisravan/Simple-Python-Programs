class AccountHolder:
    def __init__(self):
        self.AccountNumber = 12344556789
        self.__balance = 246532
        self.__password = 1919
    def setpassword(self, p):
        self.__password = p
    def getpassword(self):
        return self.__password
a = AccountHolder()
print(a._AccountHolder__balance)
