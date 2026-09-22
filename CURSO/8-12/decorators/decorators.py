# Es una funcion que extiene el comportamiento de otra

def add_sprinkles(func):
    def wrapper(*args, **kwards):
        print("You add sprinkles *")
        func(*args, **kwards)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwards):
        print("You add fudge")
        func(*args, **kwards)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your {flavour}ice cream")
    
get_ice_cream("vanilla")