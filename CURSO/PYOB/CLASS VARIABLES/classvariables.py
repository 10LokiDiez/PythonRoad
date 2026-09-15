class Student:
    class_year = 2024 #class variable

    num_students = 0
    def __init__(self, name,age):
        Student.num_students += 1 # Se utiliza en nombre de la clase para aquella class variables
        self.name = name
        self.age = age


estudiante1 = Student("Simon", 29)
estudiante2 = Student("Nicolas",26)

print(estudiante1.name )
print(estudiante2.age )

print()

print(estudiante1.class_year)
print(Student.class_year)
print(f"Hay {Student.num_students} Estudiantes")