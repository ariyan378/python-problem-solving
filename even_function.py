def even(l):
    
    even = []
    
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            pass
    return even

l = [1,2,3,4,5,6,7,8,9,10]
even(l)
        