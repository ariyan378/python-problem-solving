
# Taking Input from user

import math

h = int(input('Enter tank height :'))
l = int(input('Enter tank lenth :'))
b = int(input('Enter tank breadth :'))
h1 = int(input('Enter Glass height :'))
r = int(input('Enter  Glass radius :'))

#sise of Milk tank 

tank  =  ( h*l*b)

#size of a glass 
glass = math.pi *r**2*h1

#amount of class of milk

amount = int(tank /glass)

#result printing

print('Amount of Glass of water : ' , amount)



