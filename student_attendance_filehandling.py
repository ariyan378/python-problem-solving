import os

file_name = 'Student.txt'

print('How Many names do you want to add:')
choice = int(input())
names = set()

for i in range(choice):
    entry = input(f'Enter Name { +1}: ').strip().capitalize()
    names.add(entry)

if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        entry_count = len(lines) + 1
else:
    entry_count = 1

names_string = ", ".join(names)

with open(file_name, 'a') as f:
    f.write(f"Entry No {entry_count} -> {names_string}\n")

print(f"\n--- Success! Entry {entry_count} saved ---")

print("\n--- Current Student.txt Content ---")
with open(file_name, 'r') as f:
    print(f.read())