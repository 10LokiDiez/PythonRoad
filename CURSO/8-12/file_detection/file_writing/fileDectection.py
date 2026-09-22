import os

#    es un metodo para juntar cosas, y convertirlo en una direccion despues 
#    con el dirname trae el nombre del archivo en el que estamos, y concatena ya lo siguiente
file_path = os.path.join(os.path.dirname(__file__), "stuff", "test.txt")

if os.path.exists(file_path):
    
    print(f"The file {file_path} exist")
    
    if os.path.isfile(file_path):
        print("is a file")
        
    elif os.path.isdir(file_path):
        print("is a folder")
        
else:
    print(f"The file {file_path} doesnt exist")