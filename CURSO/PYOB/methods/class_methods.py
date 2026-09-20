class Student:
    
    count = 0
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    #INSTANCE METHOD / METODOS DE INSTANCIA sirve para la operaciones con las instancias del objeto
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    
    #CLASS METHOD sirve para cuando estamos utilizando info del nivel de la clase que seria el count y el total_gpa
    @classmethod
    def get_count(cls):
        return f"Numero de estudiantes = {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Promedio gpa: {cls.total_gpa / cls.count}"
        
    
student1 = Student("Simon", 5)
student2 = Student("jUAN", 4.3)

print(Student.get_count())
print(Student.get_average_gpa())