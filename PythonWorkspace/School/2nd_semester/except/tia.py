class InsufficienBalanceError(Exception):
    pass

class WrongAccountNumberError(Exception):
    pass

class Account:
    lastAccountNumber = 0
    accountList = []

    # @staticmethod
    @classmethod
    def newAccountNumber(cls, obj):
        cls.accountList.append(obj)
        cls.lastAccountNumber += 1
        return cls.lastAccountNumber
    
    def __init__(self, initMoney=0):
        self.number = Account.newAccountNumber(self)
        self.balance = initMoney
        self.isActive = True

    def getAccountNumber(self):
        return self.number
    
    def getBalance(self):
        return self.balance

    def addMoney(self, amount):
        self.balance += amount

    def send(self, amount, toAccount):
        if self.balance < amount:
            raise InsufficienBalanceError('Balance is not enough')
        elif toAccount.newAccountNumber() < 0 or toAccount.newAccountNumber() == self.number \
            or Account.lastAccountNumber[toAccount.getAccountNumber()] == False:
            raise WrongAccountNumberError('Wrong Account Number..')
        else:
            self.balance -= amount
            toAccount.addMoney(amount)

    def __str__(self):
        return f'Account: {self.number}, Balance: {self.balance}'

try:
    a = Account(10000)
    b = Account(20000)

    print(a)
    print(b)

    b.send(20000, a)

    print(a)
    print(b)

except InsufficienBalanceError as e:
    print(e)

except WrongAccountNumberError as e:
    print(e)