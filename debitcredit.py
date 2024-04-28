#Create a account class having attribute bank balance and account number.Also create a method for debit payment ,credit payment and printing balance.
 
class Account():
    def __init__(self,bal,accn):
        self.balance=bal
        self.account_number=accn
        
    #Debiting money
    def debit(self,amount):
     self.balance-=amount
     print("Hello,Rs",amount,"has been debited from your account")
     print("The remaining balance is",self.balance)
     
     #Crediting money
    def credit(self,amount1):
        self.balance+=amount1
        print("Hello,Rs",amount1,("has been credited in your account"))
        print("The remaining balance is",self.balance)
     
        
a1=Account(100000,123456789)
a1.debit(10)
a1.credit(10000)