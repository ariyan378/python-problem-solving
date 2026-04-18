import random

class ValueTooLarge(Exception):
    def display(self):
        print("Too Large number")
class ValueTooSmall(Exception):
    def display(self):
        print("Too Small number")
class Guesserror(Exception):
    def display(self):
        print("Number must be greater than 0")

number = random.randint(1,100) 
while 1:
    try:
        guess = int(input("Enter a number between 1 to 100 : "))
        if number<1:
            raise Guesserror
        
        if guess>number:
            raise ValueTooLarge
        if guess == number:
            print("Winner")
            break
        if number>guess:
            raise ValueTooSmall

    except ValueTooLarge as L:
        L.display()
    except ValueTooSmall as S:
        S.display()
    except Guesserror as g:
        g.display()
        