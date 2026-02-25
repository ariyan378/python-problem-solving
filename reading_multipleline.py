f = open('Sample.txt','r')

while True:
    
    my_data = f.readline()
    
    if my_data == '':
        break
    else:
        print(my_data , end='')
f.close()        
    