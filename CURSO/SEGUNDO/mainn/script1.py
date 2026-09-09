from script2 import * #everything ### or  import script2
def favourite_food(food):
    print(f"your favourite food is {food}")

def main():
    print("THIS IS SCRIPT 1")
    favourite_food("pizza")
    script2.favourite_drink("tea")
    print("Goodbye!")

if __name__ == '__main__':
    main()



