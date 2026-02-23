list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

tuple_count = 0 
list_count = 0 
set_count = 0 

for item in list1:
    if isinstance(item , tuple):
        tuple_count+=1
    elif isinstance(item , list):
        list_count +=1
    elif isinstance(item , set):
        set_count +=1

print(f" tuple : {tuple_count}")
print(f" list : {list_count}")
print(f" set : {set_count}")

