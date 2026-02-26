class bankaccount:
    
    def __init__(self , name , accountNumber ,  balance):
        self.accountNumber = accountNumber
        self.name = name 
        self.balance = balance
        
    def display(self):
        
        print(' Account Number' , self.accountNumber)   
        print(' Account Name ', self.name) 
        print('Account Balance', self.balance)
        
    def deposit(self, amount):
         self.balance = self.balance + amount
    
    def withdraw(self, amount):
        if amount>= self.balance:
            print('Insufficient balance') 
        else:
            self.balance-= amount 
            reduction = self.bankFees
            self.balance -= reduction
    
    def bankFees(self):
        
        return 0.05 * self.balance

cust = bankaccount('Ariyan Islam Hridoy' ,1 ,1500)
cust.deposit(500)
cust.withdraw(100)
cust.display()
