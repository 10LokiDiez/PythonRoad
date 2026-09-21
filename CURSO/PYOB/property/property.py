#Sirven para agregarle algo addicional a la logica, puede ser leer, escribir o eliminar atributos
class Rectangle:
    def __init__(self, width, height):
        self._width = width #el dash antes de es para declarar que son privados
        self._height = height
        
    #SIRVE PARA AGREGARLE ALGO MAS AL IMPRIMIR EL WIDTH, O PUEDE SERVIR A AGREGARLE MAS LOGICA
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    #SIRVEN PARA AYUDAR A SETEAR NUEVOS VALORES DE WIDTH SABIENDO QUE TIENEN UNA CONDICION
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Your width most be greater than 0")
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print("Your height most be greater than 0")

    #PROPIEDADES QUE AYUDAN A AGREGAR ALGO MAS A ELIMINAR UN VALOR
    @width.deleter
    def width(self):
        del self._width
        print("The width has been deleted")
        
        
    @height.deleter
    def height(self):
        del self._height
        print("The height has been deleted")
    
rectagle1 = Rectangle(3,4)

print(rectagle1.width)
print(rectagle1.height)

rectagle1.width = 10
rectagle1.height = 0

del rectagle1.width