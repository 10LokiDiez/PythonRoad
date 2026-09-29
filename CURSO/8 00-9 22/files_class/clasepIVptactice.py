#MANEJO DE ARCHIVOS
# .txt .json .csv .xlsx
from io import *
import os

path = r"C:\Users\sidim\Escritorio\Programacion IV\CURSO\8-12\files_class\registro.txt"

if not os.path.exists(path):
    archivo = open(path, "w")
    archivo.close()

archivo = open(path, "a")
while True:
    nombre = input("Ingrese su nombre o 0 para finalizar: ")
    if nombre == "0":
        break
    else:
        edad = int(input("Ingrese su edad: "))
        archivo.write("Nombre: "+ nombre+ ", Edad: "+ str(edad) +"\n")
        
archivo.close()
archivo = open(path, "r")
lect = archivo.read()
print(lect)