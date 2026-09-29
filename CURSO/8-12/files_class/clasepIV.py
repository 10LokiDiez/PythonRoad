#MANEJO DE ARCHIVOS
# .txt .json .csv .xlsx

import os

file_path = os.path.join(os.path.dirname(__file__), "test.txt")

print(file_path)

with open(file_path, "w") as file:
    file.write(file_path)