class Atm:
    
    
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
    
    def menu(self):
        print('''
        
        Hi ! How Can I Help You
        1 = Create Pin
        2 = Change Pin
        3 = Check Balance
        4 = withdraw
        5 = Anything Else To Exit \n''')
        
        user_input = input('1/2/3/4/5 : ')
        
        
    
        if user_input =='1':
            self.create_pin()
        if user_input =='2':
            self.change_pin()
        if user_input =='3':
            self.check_balance()
        if user_input =='4':
            self.withdraw()
        if user_input =='5':
            exit
        
    
    def create_pin(self):
        
        user_pin = input('Enter Your Pin : ')
        self.pin = user_pin
        
        user_balance = int(input(' Enter Your Balance :'))
        self.balance = user_balance
        
        print('Your Print Created Successfully ')
        
        self.menu()
    
    def change_pin(self):
        
        old_pin = input('Enter Your Old :')
        
        if old_pin == self.pin:
            new_pin = input('Enter Your New Pin : ')
            self.pin = new_pin
            print("Pin Changed Successfully")
        
        else:
            print("Wrong Pin")
        
        self.menu()  
            
    def check_balance(self):
        
        user_pin = input("Enter Your Pin :")           
        
        if user_pin == self.pin:
            print('Your Current Balance Is ' , self.balance)
        
        else:
            print("Invalid Pin")
        
        
        self.menu()
    
    def withdraw (self):
        
        user_input = input('Enter your Pin :')
        
        if user_input == self.pin:
            amount = int(input('Enter Amount :'))
            
            if self.balance >= amount:
                self.balance = self.balance - amount
                print("Withdraw Done !! Your Current Balance Is " , self.balance)
            
            else:
                print("Insufficient Balance ")
        else:
            print('Wrong pin')
        
        self.menu()                
        
if __name__ == "__main__"    :
    
    Final =Atm()
        
        



    

