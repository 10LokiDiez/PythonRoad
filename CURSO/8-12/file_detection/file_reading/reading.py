file_path = "C:/Users/sidim/Escritorio/Programacion IV/CURSO/8-12/file_detection/file_writing/stuff/test.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")