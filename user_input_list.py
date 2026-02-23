# Make an empty list to store our items
my_list = []

# Ask the user to add items
print("Let's make a list! Type 'stop' when you're done.")

# Keep asking for items until they say 'stop'
while True:
    item = input("Add something to your list: ")
    
    if item == 'stop':
        break
    
    my_list.append(item)

# Show everything in the list
print("\nHere's your list:")
print(my_list)