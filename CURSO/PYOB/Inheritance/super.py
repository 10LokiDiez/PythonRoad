#
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"You have a {self.color} and {"filled" if self.filled else "not filled"}")
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled) #En vez de super() se puede poner Shape.__init__(color,filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, side):
        super().__init__(color, filled)
        self.side = side
        
    def describe(self):
        print(f"It has a {self.side}")
        super().describe()
class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
        
    
circle1 = Circle(color="red", filled=True, radius=5)

print(circle1.radius)
print(circle1.filled)
print(circle1.color)
circle1.describe()


square2 = Square("Blue", False, 5)

square2.describe()