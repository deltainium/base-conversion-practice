from random import randint

def user_input() -> tuple:
    command = None

    while 1:
        command = input("How many digits would you like the decimal to have? (input q to quit)\n")

        if command == "q":
            exit()

        try:
            digits = int(command)
            break

        except:
            print("Invalid input, please try again\n")
            continue
 
    acc = ("binary", "hex")

    while 1:
        command = input("Binary or hex?\n").lower()

        if command not in acc:
            print("Invalid input, please try again\n")
            continue
        else:
            base = str(command)
            break



    return (digits, base)

def challenge(digits: int, base: str):
    lower_bound = int("1"*digits)
    upper_bound = int("9"*digits)

    number = randint(lower_bound, upper_bound)
    if base == "binary":
        target = bin(number)[2:]
    else:
        target = hex(number)[2:]
    
    while 2:
        answer = input(f"What will {number} be in {base}? (q to quit)\n").lower()

        if answer == target:
                while 1:
                    command = input("Correct! Try again? (y/n)\n")
                    acc = ("y","n")

                    if command not in acc:
                        print("Invalid input, please try again")
                        continue
                    else:
                        if command == "y":
                            challenge(digits, base)
                        else:
                            exit()

        elif answer == "q":
            exit()

        else:
            print("Incorrect, please try again")
            continue


if __name__ == "__main__":
    digits, base = user_input()
    challenge(digits, base)
