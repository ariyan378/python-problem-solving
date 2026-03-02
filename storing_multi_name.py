print('How Many name you want to add :')
choice = int(input())
name = set()

for i in range (0,choice):
    entry = input('Enter Your Name :').strip().capitalize()
    name.add(entry)
    
print('Student List :')    
print(name)  

with open('Student.txt', 'a') as f :
    f.writelines(f"{name}\n")

with open('Student.txt', 'r') as f :
    std = f.read()
    print(std)