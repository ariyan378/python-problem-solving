try :
    with open('text1.txt', 'w') as f:
        f.write('Good morning')
except IOError:
    print('Some error have occured')
else:
    print("File updated succesfully")            
    
        