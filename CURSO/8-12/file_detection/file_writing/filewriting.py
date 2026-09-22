import os

txt_data ="I like H2332amburguers"

file_path = os.path.join(os.path.dirname(__file__), "stuff","output.txt")
employees = ["Eugene", "Martin", "Josh", "Santi", "Loki"]

print(file_path)
#w write, a append, r read, x write without a txt created
try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(txt_data)
            file.write(f" {employee} \n")
            
        print(f"txt file output.txt was creatted")
except FileExistsError:
    print("That file already exist")