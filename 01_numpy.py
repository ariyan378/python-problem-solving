###`Q-3`Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array shape as (a,b) as parameter to function.

# Eg.-

# [[1,1,1,1],
# [1,0,0,1],
# [1,0,0,1],
# [1,1,1,1]]

import numpy as np

def array_border(a,b):
    arr = np.zeros((a,b), dtype=int)
    
    arr[0,:]=1 #top
    arr[-1,:]=1#bottom
    arr[:,0]=1
    arr[:,-1]=1
    
    return arr

print(array_border(5,5))
