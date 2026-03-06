#  Write a python function which infinitely prints natural numbers in a single line. Raise the StopIteration exception after displaying first 20 numbers to exit from the program.

def display(n):
    i = 0 
    
    while True:
        try:
            i+=1
            n+=1
            if i==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n, end=',')    

display(22)