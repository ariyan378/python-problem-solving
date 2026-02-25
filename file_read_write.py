f = open('Sample.txt' , 'w')

Quote = "You don't grow when you are comfortable"

f.write(Quote)

f = open('Sample.txt' , 'r')

Txt  = f.read()

print(Txt)

f.close()