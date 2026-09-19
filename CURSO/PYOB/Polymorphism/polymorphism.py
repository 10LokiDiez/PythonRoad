#Poly = many
#Morphe = Form

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
        
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius **2 *3.1416
    
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
    
class Triangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height/2 * self.width

class Pizza(Circle):
    def __init__(self,topings,radius):
        self.topings = topings
        super().__init__(radius)

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Peperonni", 50)]

for shape in shapes:
    print(f"The area of the {shape} is: {shape.area(): .2f}cm2")