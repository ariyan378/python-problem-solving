l = ([5,6] , (5,7),(5,8),(6,10),(7,13))

grouped_element = {}#its a dictionary

for item in l :
    first_element  = item[0]
    if first_element in grouped_element:
        grouped_element[first_element].extend(item[1:])
    else :
        grouped_element[first_element] = list(item[1:])


output = []

for key , value in grouped_element.items():
    output.append(tuple([key]+value))

print(f" Output is : {output}")    
