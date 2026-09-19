#Permite heredar cosas de un padre
class Predator:
    def predate(self):
        print(f"{self.name} is predating")
        
class Animal:
    def __init__(self, name): #constructor
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} esta comiendo")

    def sleep(self):
        print(f"{self.name} esta durmiendo")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meaw")

class Mouse(Animal, Predator):
    def speak(self):
        print("squeek")


dog1 = Dog("Scooby")

cat1 = Cat("Garfield")

mouse1 = Mouse("Mickey")

print(dog1.name)
cat1.sleep()
mouse1.eat()

dog1.speak()
cat1.speak()
mouse1.speak()

mouse1.predate()