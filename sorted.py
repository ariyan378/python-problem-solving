def Sort_sequence(s):
    
    temp =[]
    
    for i in sorted(s.split('-')):
        temp.append(i)
        
    return '-'.join(temp)

s =   'green-red-yellow-black-white'  
Sort_sequence(s)