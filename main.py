from random import randint

def user_input() -> int:
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

    return digits

def challenge(digits):
    lower_bound = int("1"*digits)
    upper_bound = int("9"*digits)

    number = randint(lower_bound, upper_bound)
    target = bin(number)[2:]
    
    while 2:
        answer = input(f"What will {number} be in binary? (q to quit)\n")

        if answer == target:
                while 1:
                    command = input("Correct! Try again? (y/n)\n")
                    acc = ("y","n")

                    if command not in acc:
                        print("Invalid input, please try again")
                        continue
                    else:
                        if command == "y":
                            challenge(digits)
                        else:
                            exit()

        elif answer == "q":
            exit()

        else:
            print("Incorrect, please try again")
            continue

def main():
    digits = user_input()
    challenge(digits)

if __name__ == "__main__":
    main()
