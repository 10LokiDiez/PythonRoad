import random
import string

def encript(chars, copy_chars):
    plain_text = input("Inserte su texto: ")
    cipher_text = ""
    
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += copy_chars[index]
    
    
    print(cipher_text)


def desencript(chars, copy_chars):
    plain_text = input("Inserte su texto: ")
    cipher_text = ""
    
    for letter in plain_text:
        index = copy_chars.index(letter)
        cipher_text += chars[index]
    
    
    print(cipher_text)

def main():
    chars = string.ascii_letters + " " + string.digits  + string.punctuation 
    chars = list(chars) #convierte cada caracter en una lista
    copy_chars = chars.copy()
    
    random.shuffle(copy_chars)
    
    print (f"chars: {chars}")
    print (f"copy: {copy_chars}")
    while True:
        print("**************Programa Encriptador Basico***************")
        print("1. Encriptar")
        print("2. Desencriptar")
        print("3. Salir")
        op = int(input("Elige una opcion:  "))
        match op:
            case 1:
                encript(chars, copy_chars)
            case 2:
                desencript(chars, copy_chars)
            case 3:
                break
            
            case _:
                print("Opcion Erronea")
    print("Saliendo...")
            


if __name__ == '__main__':
    main()


main()