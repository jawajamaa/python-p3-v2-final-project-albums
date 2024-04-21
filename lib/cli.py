# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    helper_2
)


def main():
    while True:
        menu()
        choice = input(">")
        if choice == "e":
            exit_program()
        elif choice == "q":
            exit_program()
        else:
            print("Please choose another option")

def menu():
    print("Please select an option")
    print("Press e or q to exit the program")
    print("Some pointless function")

if __name__ == "__main__":
    main()
