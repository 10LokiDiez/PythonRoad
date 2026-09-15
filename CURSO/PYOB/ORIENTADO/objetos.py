from CURSO.PYOB.ORIENTADO.car import Car
#Un objeto tiene atributos (Variables) y metodos (funciones) son como las cosas que puede hacer el objeto

#Para crear varios objetos con atributos y funciones, se crea una clase
#Que es un diseño del objeto

carropapa = Car("Hylux", 2020, "Gray", True)
carromama = Car("Duster",2013,"Gray", False)

print(carropapa)
print(carropapa.model) #. es el operador de los atributos
print(carropapa.year)
print(carropapa.color)
print(carropapa.for_sale)

print()

print(carromama.model) #. es el operador de los atributos
print(carromama.color)
print(carromama.year)
print(carromama.for_sale)

print()

carropapa.stop()
carromama.drive()
carromama.description()