import os

file  = "1st.json"

if os.path.exists(file):
    os.remove(file)
else:
    print("The file doesn't exist")    