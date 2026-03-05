class securityerror(Exception):
    
    def __init__(self , msg):
        print(msg)
    
    def logout(self):
        print('Login Error')

class Google :
    
    def __init__(self, name ,email , password , device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device
        
    def login(self , email, password , device):
        
        if self.device!=device:
            raise securityerror('Invalid Device')
        if self.email==email and self.password==password:
            print("login succesful")
        else:
            print('Logout')
            
obj = Google ('Hridoy' , 'ariyanhridoy121@gmail.com','123456789' , 'Poco M4 ')

try:
    obj.login( 'ariyanhridoy121@gmail.com','123456789' , "windows")
except securityerror as e:
    e.logout() 
else:
    print('Logout')
finally:
    print('Database connection failed')                      
                 
                   
