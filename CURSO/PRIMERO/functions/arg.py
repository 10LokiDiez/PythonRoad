#DEFAULT ARGUMENTS
def final_price(list_price, discount = 0, tax= 0.05):
    return list_price * (1-discount) * (1 + tax)

print(f"{final_price(500, 0.8, 0.5):.2f}" )
print(f"{final_price(500, 0.1):.2f}" )


def hello(greating, title, first,last):
    print(f"{greating} {title}{first} {last}")

#KEYWORD ARGUMENT
hello("Hello", first="Simon", title="Mr.", last="Diez")
#El print tambien tiene keyword arguments ej: end=" "
print("1", "2", "3","4","5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

print(get_phone(country="57", area="321", first="342", last="3534"))