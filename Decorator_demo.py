import time

def timer(func):
    
    def wrapper(*args):
        start = time.time()

        func(*args)

        print('Time Taken By', func.__name__ , time.time()-start , 'secs')
        print("___________________")
    
    return wrapper

@timer
def hello():
    
    print('Hello Himuuuu') 
    time.sleep(1)
    
@timer
def Barcelona():
    
    print("Lionel Messi The Goat") 
    time.sleep(1)   

@timer
def square (num):
    
    time.sleep(1)
    print(num**2)    


hello()    
Barcelona()
square(111)   