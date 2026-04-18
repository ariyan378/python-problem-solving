# Write a program that validate name and age as entered by the user to determine whether the person can cast vote or not. To handle the age, create InvalidAge exception and for name, create InvalidName exception. The name will be invalid when the string will be empty or name has only one word.

class InvalidAge(Exception):
    def Display(self):
        print("Invalid Age ")
        
class InvalidName(Exception): 
    def Display(self):
        print("Invalid Name ")

try:     
    
    name = input('Enter Your name :\n')       
    age = int(input('Enter Your age :\n')) 
         
    if age < 18 :
        raise InvalidAge
    if len(name)==0 or len(name.split())<2:
        raise InvalidName
    else:
        print('Valid Voter')
        
        
except InvalidAge as A:
    A.Display()     
       
except InvalidName as N:
    N.Display()  
else:
    print('Vote done succesfully')
finally:
    print("Thank you")              

           