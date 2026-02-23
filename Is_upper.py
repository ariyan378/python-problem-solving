def Count_upper_lower(s):
    
    upper=0
    lower=0
    
    for i in s :
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            pass
    return upper , lower             
       



s =' CampusX is an Online Mentorship Program fOr EnginEering studentS.'
x,y = Count_upper_lower(s)
print(x)
print(y)