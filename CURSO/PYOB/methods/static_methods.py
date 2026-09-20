class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    
    def get_info(self):
        return f"Your name is {self.name} and you job is {self.job}"

    #Sirven para funciones que no necesitan de info como tal de la clase
    @staticmethod
    def is_valid_job(job):
        valid_position = ["Manager","Cashier","Cook","Janitor"]
        return job in valid_position 
    
#Sirve para tener un metodo que se puede usar sin tener un objeto ya establecido
print(Employee.is_valid_job("Cook"))