class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self,amount):
        if amount < 0:
            
            raise Exception('negative Money!!!')
        
        if self.balance < amount:
            raise Exception('Low Balance')
        
        self.balance += amount
        
        
obj = Bank(102)

try :
    obj.withdraw(20202)
except Exception as e :
    print(e)
else:
    print(obj.balance)            