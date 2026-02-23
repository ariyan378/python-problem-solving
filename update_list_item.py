candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

# Using zip to combine candy names with their quantities
for candy, quantity in zip(candy_list, no_of_items):
    print(f"{candy}-{quantity}")