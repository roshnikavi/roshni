class bank:
    def __init__(self,accountnum,balance):
        self.accountnum=accountnum
        self.balance=balance
        print("account created with the number:",accountnum)
        print("initial balance:",self.balance)

    def dis_balance(self):
        print("your account balance:",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("amount deposited:",amount,"available balance:",self.balance)

    def withdraw(self,withamount):
        if self.balance<withamount:
            print("insufficient balance")
        else:
            self.balance("amount withdraw:",withamount)

class savings(bank):
    def __init__(self,accountnum,balance,interest):
        super().__init__(accountnum,balance)
        self.interest=interest
    def applyinterest(self):
        interest=self.balance*(self,interest/100)
        self.balance+=interest
        print("applied interest:",interest)
        print("total balanc with interest:",self.balance)

obj=savings(123,1000,5)
obj=deposit(500)
obj=withdraw(300)
obj.dis_balance()
sav.applyinterest()
