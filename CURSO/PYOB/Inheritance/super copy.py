#CLASE PADRE
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print("TE VOY A DESCRIBIR TU FIGURA!!!!!")
        print(f"You have a {self.color} color shape and {"is filled" if self.is_filled else "not is filled"}")
       
       
#CLASES HIJAS 
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) #En vez de super() se puede poner Shape.__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It has a {self.radius} radius and a area of {self.radius **2 * 3.1416}")
            
    
class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side
        
    def describe(self):
        super().describe()
        print(f"It has a {self.side} side and a area of {self.side ** 2}")
        
        
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
    def describe(self):
        super().describe()
        print(f"The width of this Shape is: {self.width} and the height is: {self.height} and it has an area of {(self.width/2)*self.height}")
        
    
circle1 = Circle(color="Red", is_filled=True, radius=5)
print(circle1.radius)
print(circle1.is_filled)
print(circle1.color)
circle1.describe()


square2 = Square("Blue", False, 5)
square2.describe()

triangle3 = Triangle("Green", True, 4, 6)
triangle3.describe()