import random

def gamb(sym):
    nums = [random.randint(0,4) for _ in range(0,3) ]
    print("*************")
    for num in nums:
        print(f"{sym[num]}",end="  ")
    print()
    print("*************")
    if nums.count(nums[0]) == 3:
        return True
    else:
        return False


def main():
    print("*******************************")
    print("Bienvenido al juego de gambling")
    print("Symbolos: 🍒  🍉  🍊  🔔  ⭐")
    print("*******************************")
    symbols = ["🍒","🍉","🍊",'🔔',"⭐"]
    balance = 100
    is_running = True
    while is_running:
        print(f"Balance actual {balance}$")
        if balance == 0:
            break
        bet = input("Ingrese su apuesta: ")
        if not bet.isdigit():
            print("Error, no es un digito")
            continue
        bet = int(bet)
        if bet <= 0:
            print("Vuelve a intentarlo, es mayor a 0")
            continue
        elif bet > balance:
            print("Vuelve a intentarlo, no tienes tanto dinero...")
            continue
        else:
            print("Girando...", end ="\n\n")
            if gamb(symbols):
                balance += bet * 10
                print(f"Ganaste {bet*10}")
            else:
                balance -= bet
                print("Perdiste esta ronda")
                
            ind= input("Quieres volver a Jugar (S/N)?: ").lower()
                
            if ind == "s":
                continue
            else:
                break
            
    print("MUCHAS GRACIAS!!")
                
                


if __name__ == '__main__':
    main()