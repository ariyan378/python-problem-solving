class Computation:
    
    def __init__(self ):
        
        pass
    
    def Factorial(self , n ):
        j = 1
        
        for i in range(1,n+1):
            j = j*i
            
        return j
    
    def natural_number(self, n):
        a=0
        
        for i in range(1 , n+1):
            a = a+i
        return a    

        
    
c1 = Computation()
result = c1.Factorial(6)
print(result)   
print(c1.natural_number(2))    
