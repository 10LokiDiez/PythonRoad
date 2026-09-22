import json
file_path = "C:/Users/sidim/Escritorio/Programacion IV/CURSO/8-12/file_detection/file_writing/stuff/output2.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
        
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")