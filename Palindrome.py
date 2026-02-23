s = input('Enter Your String :')
Flag = True

for i in s(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        print("Is Not Palindrome")
        break

if Flag:
    print("YES! It is a paindrome")

