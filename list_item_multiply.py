tuple1 = (1,5,7,8,10)

result = []


for i in range (len(tuple1)):
    if i ==0:#1st element
        result.append( tuple1[i]*tuple1[i+1])
    elif i == len(tuple1)-1:#last element
        result.append( tuple1[i]*tuple1[i-1])
    else :#middle elements
        result.append(tuple1[i]*tuple1[i-1]+tuple1[i]*tuple1[i+1])

print(result)