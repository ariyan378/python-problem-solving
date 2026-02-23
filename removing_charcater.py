s = input("Enter Your String :")
term =input('Enter The character you want to remove :')
result= ''
for i in s :
    if i!=term:
        result+=i

print(result)