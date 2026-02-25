import random

class Flashcard:
    
    def __init__(self):
        
        self.fruits={
            'apple':'red',
            'banana':'yellow',
            'watermelon':'green',
            'strawberry':'pink',
            'guava':'green'  
        }

    def quiz(self):
        while True:
            fruit,color = random.choices(list(self.fruits.items()))[0]
            print('What is the color of {} -- \n'.format(fruit)) 
            user_input=input()
        
            if user_input.lower()==color:
                print('correct')
            else:
                print("incorrect")      
                
            option = int(input())
            if option:
                break

print("welcome to the fruit Game")
fc = Flashcard()
fc.quiz()            
            