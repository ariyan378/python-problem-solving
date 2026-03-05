class MyException(Exception):
    
    def __init__(self, message):
        
        super().__init__( message)
        
class Bank:

  def __init__(self,balance):
    self.balance = balance

  def withdraw(self,amount):
    if amount < 0:
      raise MyException('amount cannot be -ve')
    if self.balance < amount:
      raise MyException('paise nai hai tere paas')
    self.balance = self.balance - amount

obj = Bank(900)
try:
  obj.withdraw(1000)
except MyException as e:
  print(e)
else:
  print(obj.balance)        
        