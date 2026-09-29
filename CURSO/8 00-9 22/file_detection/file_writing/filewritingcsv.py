import os
import csv
employees = [["Name","Age","Job"],
            ["Spongebob", 30, "Cook"],
            ["Patrick", 36, "Unemployed"],
            ["Sandy", 27, "Scientist"]]
file_path = os.path.join(os.path.dirname(__file__), "stuff","output2.csv")

print(file_path)
    
try:
    with open(file_path, "w", newline="") as file:
        writer=csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"txt file output.csv was creatted")
except FileExistsError:
    print("That file already exist")