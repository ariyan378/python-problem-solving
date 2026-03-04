try :
    f =  open ('demo1.txt','r') 
except FileNotFoundError:
    print("File pacchina") 
    
else:
    data = f.read()
    print(data)
finally:
    print('Sick')                