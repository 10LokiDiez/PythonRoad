import random

def gamb(sym):
    nums = [random.randint(0,4) for x in range(0,3) ]
    print("*************")
    for num in nums:
        print(f"{sym[num]}  ", end=" ")
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
        bet = int(input("Ingrese su apuesta: "))
        if bet <= 0:
            print("Vuelve a intentarlo, es mayor a 0")
            pass
        elif bet > balance:
            print("Vuelve a intentarlo, no tienes tanto dinero...")
            pass
        else:
            print("Girando...", end ="\n\n")
            if gamb(symbols):
                balance += bet * 10
                print(f"Ganaste {bet*10}")
            else:
                balance -= bet
                print("Perdiste esta ronda")
            is_running == True if input("Quieres volver a Jugar (S/N)?: ").lower() == "s" else is_running == False


if __name__ == '__main__':
    main()