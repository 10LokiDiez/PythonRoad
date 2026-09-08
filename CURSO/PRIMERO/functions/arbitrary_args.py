"""
*args    /arguments to a tuple (non-key arguments)
**kwargs /keywords arguments to a dictionary (keyword arguments)

* unpacking operator
"""

"""def add(x,y):
    return(x+y)

print(add(1,2,3))"""

####################### ARGS ###########################
#SE PUEDE CAMBIAR EL NOMBRE DE *args A POR EJ: *nums
def add(*args):
    print(type(args))
    total = 0
    for arg in args:
        print(arg)
        total += arg
    return total

print(f"TU RESULTADO ES: {add(1,2,3,20, 4)}")


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print(end= "\n\n")

display_name("Simon", "Beatriz", "Juaquin", "Julian")



####################### kwargs ###########################
def direccion(**kwargs):
    print(type(kwargs))
    for val in kwargs.values():
        print(val)

    print()
    for key in kwargs.keys():
            print(key)

    print()
    #### o de la siguiente manera

    for key, val in kwargs.items():
        print(f"KEY: {key:7} VALUE: {val}")


direccion(street= "234 Esme St.", city = "Pasto", state = "Mesmer Land", zip ="66412")

#SE PUEDEN USAR LAS DOS