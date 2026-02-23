str1 = input("Enter Your String : ")

middle = len(str1)//2

if str1[:middle]==str1[middle:]:
    print("The string is symmetrical")
else:
    print("The string is not symmetrical")



'''s='hridoy'
middle = len(s)//2
print(s[:middle])
print(s[middle:])'''