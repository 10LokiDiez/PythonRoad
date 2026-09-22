import csv
file_path = "C:/Users/sidim/Escritorio/Programacion IV/CURSO/8-12/file_detection/file_writing/stuff/output2.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for row in content:
            for it in row:
                print(f" {it:10} |", end="" )
            print()
            

        
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")