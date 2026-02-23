def return_unique(L):
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)

    return L1    

        
L = [1,22,22,3,4,565,323,3,3,3,3]
print(return_unique(L))            
               