def show_balance():
    print(f"Su saldo es: {balance}$", end="\n\n")

def deposit():
    
    num = float(input("Ingrese cuanto quiere ingresar: "))
    if num> 0:
        print(f"Ha ingresado {num}$", end="\n\n")
        return num
    else:
        print(f"Error, vuelvalo a intentar", end="\n\n")
        return 0
    

def withdraw():
    num = float(input("Ingrese cuanto quiere sacar: "))
    
    if num > balance:
        print(f"Error, Saldo Insuficiente", end="\n\n")
        return 0
    elif num < 0:
        print(f"Error, vuelvalo a intentar", end="\n\n")
        return 0
    else:
        print(f"Ha retirado {num}$", end="\n\n")
        return num
    
def main():
    balance = 0

    while True:
        print("====Programa de Cajero====")
        print("1. Mostrar el saldo")
        print("2. Depositar saldo")
        print("3. Sacar saldo")
        print("4. Salir")
        choice = int(input("Ingrese la opcion que desee(1-4): "))
        
        match choice:
            case 1:
                show_balance()
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw()
            case 4:
                break
            case _:
                print("Dato erroneo, Vuelva a intentarlo")
                pass
            
    print("MUCHAS GRACIAS!!")
    
    
if __name__ == '__main__':  
    main()