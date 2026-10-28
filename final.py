from pyfiglet import Figlet


class Product:
    def __init__(self, id_product, name, price, quantity):
        self.id_product = id_product
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def get(cls, id):

        """
        ClassMethod
        It creates new products, validating each atribute of the class
        """
        name = input("Which is the name of the product?: ")
        while True:
            try:
                price = int(input("Which is the price of the product?: "))
                if price >= 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid price")
        while True:
            try:
                quantity = int(input("Which is the quantity of the product?: "))
                if quantity >= 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid quantity")
        return cls(id,name,price,quantity)

class Shop:
    def __init__(self, name):
        self.name = name
        self.inventory = []


    



def get_product(shop):
    print("\n If you want to add stock, enter the ID of the product") 
    print(" If you want to add a new product, enter a unique ID") 
    print(" If you want to return to the menu, type any letter")
    try:
        id = int(input("Enter the ID: "))
    except ValueError:
        menu()
    product = Product.get(id)
    shop.inventory.append(product)
    return product

def menu():
    shopCS50 = Shop("CS50")
    while True:
        while True:
            print("-"* 18, "Welcome to the shop's menu", "-"* 18)
            print("    1- Add a new product or add stock to a product")
            print("    2- Register a sale")
            print("    3- Update or modify a product (Name/Price/Quantity)")
            print("    4- Delete a product (Danger)")
            print("    5- List of all the products")
            print("    6- Exit the program ")
            try:
                option = int(input(" Which option do you want to select: "))
                if 0 < option < 7:
                    break
                else:
                    raise ValueError
            except:
                print("\nInvalid Option, Try again...\n")
                continue
        match option:
            case 1:
                get_product(shopCS50)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("\nLeaving the program...\n")
                break
            case _:
                print("\nInvalid Option, Try again...\n")

def main():
    figlet = Figlet()
    figlet.setFont(font="puffy")
    print(figlet.renderText("==SHOP=="))
    menu()
if __name__ == "__main__":
    main()