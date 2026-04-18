class Person:
    
    def __init__(self, name):
        self.name = name

def greet(Person):

    return Person

hello = Person('Himu')

h = greet(hello)

print(h.name)   

      