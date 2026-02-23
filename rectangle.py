class Rectangle:
    
    def __init__(self , length , width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        
        return 2*(self.length+self.width)
    
    def area(self):
        return self.length *self.width
    
    def display(self):
        
        print(f"The Length is {self.length}")
        print(f"The Width is {self.width}")
        print(f"The perimeter is {self.perimeter()}")
        print(f"The Area is {self.area()}")
        
Rec = Rectangle(3,4)
Rec.display()
    