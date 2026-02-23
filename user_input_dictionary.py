sub = {}

def marks(sub1,x):
    return sub.update({ sub1 : x})

num = int(input("Enter Your subject Count :"))

for i in range (num):
    sub1 = input("Input Your Subject Name : ")
    x = int(input(f'Enter {sub1} :'))
    marks(sub1 , x)


print(sub)
print(list(sub.items()))


'''
y = int(input('Enter Artificial Intelligence :'))
sub.update({"Artificial Intelligence" : y})

z = int(input('Enter Software Engineer :'))
sub.update({"Software Engineer" : z})

a = int(input('Enter Operating System :'))
sub.update({"Operating System" : a})
'''