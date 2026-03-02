
import os

# Get the names from the user
print('How Many names do you want to add:')
choice = int(input())
names = set()

for i in range(choice):
    entry = input('Enter Your Name: ').strip().capitalize()
    names.add(entry)


file_name = 'Student.txt'
print(f'Your Current File Name -> {file_name}')

if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        # Count how many lines are already in the file
        existing_lines = f.readlines()
        entry_count = len(existing_lines) + 1
else:
    # If the file doesn't exist yet, start at 1
    entry_count = 1


with open(file_name, 'a') as f:
    # I save the set, but converting it to a list/string for the file
    f.write(f"Entry No {entry_count} -> {names}\n")

print(f"\n--- Success! Added Entry No {entry_count} ---")


print("Current File Content:")
with open(file_name, 'r') as f:
    print(f.read())