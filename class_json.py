import json
#def ask_chatgpt (prompt):
class Person:
    def __init__(self, name, id):
        self.name = name 
        self.id = id

person = Person('Hridoy', 378)

def display_object(obj): 
    if isinstance(obj, Person):
  
        return "My name is {} . My Id is {}".format(obj.name, obj.id)

with open('Object.json', 'w') as f:

    json.dump(person, f, default=display_object) 
         
with open('Object.json', 'r') as f:
    text = json.load(f)
    print(text)