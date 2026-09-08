#POSITIONAL ARGUMENT
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are old! {age}")
    print("Happy birthday to you!")
    print()
age = 20
is_name = "Simon"
happy_birthday(is_name,age)
happy_birthday(is_name,age)
happy_birthday(is_name,age)
happy_birthday(is_name,age)


def add(x,y):
    a = x + y
    return a

print(add(1,3))

name = input("Digite su nombre: ")
apel = input("Digite su apellido: ")

def full_name(name, apell):
    full = name.capitalize() + " " + apell.capitalize()
    return full

print(full_name(name, apel))