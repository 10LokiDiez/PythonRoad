class Car:
    def __init__(self, model, year, color, for_sale): #ESTO ES UN CONSTRUCTOR METODO PARA CREAR OBJETOS, EL __init__ es un dunder 
        self.model = model  #VARIABLES DE INSTANCIAS
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"Estas manejando el carro {self.model}")


    def stop(self):
        print(f"Paraste el carro {self.model}")

    def description(self):
        print(f"Tu carro es un {self.year} {self.color} {self.model}")