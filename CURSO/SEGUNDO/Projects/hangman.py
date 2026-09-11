import random
def imprimir(live, hang):
    print("***********")
    for row in hang.get(live):
        for tup in row:
            print(f"{tup}", end="")
        print()
    print("***********")


def main():
    words = ("manzana","coco", "banano", "platano", "pera", "kiwi")
    
    hang = {0:("    ",
               "    ",
               "    "),
            
            1:("  o ",
               "    ",
               "    "),
            
             2:("  o ",
                "  | ",
                "    "),
             
             3:("  o ",
                " /| ",
                "    "),
             
             4:("  o ",
                " /|\\",
                "    "),
             
             5:("  o ",
                " /|\\",
                " /  "),
             
             6:("  o ",
                " /|\\",
                " / \\")}
    
            
    live = 0
    word = random.choice(words)
    try_word = ["_" for _ in word]
    guesses = set()
    
    while True:
        if "_" not in try_word:
            print(f"Ganaste!!!! ")
            break
        imprimir(live, hang)
        if live == 6:
            print(f"Perdiste, era {word}")
            break
        for wordi in try_word:
            print(f"{wordi} ", end="")
        print()
        guess = input("Ingresa una letra: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Error, ingresa solo una letra")
            continue
        if word.count(guess) > 0:
            if guess in guesses:
                print("Ya intentaste esa letra")
                continue
            print(f"Correcto, la palabra era: {guess}")
            guesses.add(guess)
            for i in range(len(word)):
                if guess == word[i]:
                    try_word[i] = guess
        else:
            live += 1
            print("Error, palabra equivocada")

if __name__ == '__main__':
    main()