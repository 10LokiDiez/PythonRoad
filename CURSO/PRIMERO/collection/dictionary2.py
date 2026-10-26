spacecraft = {"name": "Voyager 1", "number":5}
#para acceder a alguno podriamos hacer lo siguiente
print("AQUI IMPRIME EL NOMBRE")
print(spacecraft["name"])
#si queremos agregar algo mas podriamos hacer lo siguiente
spacecraft.update({"Fuel":"Gas", "date" : "13/02/2003"})
print("AQUI IMPRIME LOS KEYS")
#Asi podemos acceder a todas las keys
for it in spacecraft:
    print(it)
    
#Entonces se puede acceder al value asi:
print("AQUI IMPRIME LOS VALUES")
for it in spacecraft:
    print(spacecraft[it])
#o
for it in spacecraft:
    print(spacecraft.get(it))
    
#y este de get tiene otra funcion
print(spacecraft.get("number", "No esta Registrado"))
print(spacecraft.get("IDK", "No esta Registrado"))

#Se pueden iterar como listas
print(spacecraft.keys())
print(spacecraft.values())

#para eliminar alguna llave podriamos hacer
key = spacecraft.pop("Fuel")
print(key)
print(spacecraft)
