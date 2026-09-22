import os
import json
employee = {
            "name" : "Simon",
            "age" : 32,
            "job" :"Engeneer"
            }

file_path = os.path.join(os.path.dirname(__file__), "stuff","output2.json")

print(file_path)

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=1)
        print(f"txt file output.json was creatted")
except FileExistsError:
    print("That file already exist")