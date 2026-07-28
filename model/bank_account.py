class bank_account:
    def __init__(self,owner,balance):
        self.awner=owner
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("deposit successful")
    def withdraw (self ,amount ):
       if amount<self.__balance:
        self.__balance-=amount
        print( "withdrawal successful")
       else:
          print("inseficient balance")
    def Get_balance(self):
       return self.__balance
