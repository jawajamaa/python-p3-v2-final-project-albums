# lib/cli.py

from helpers import (
    exit_program,
    list_all_albums,
    list_all_genres
)


def main():
    while True:
        menu()
        choice = input(">")
        if choice == "e":
            exit_program()
        elif choice == "q":
            exit_program()
        elif choice == "a":
            list_all_albums()
        elif choice == "j":
            list_all_genres()
        else:
            print("Please choose another option")

def menu():
    print(u'\u2500'* 30)
    print("Please select an option")
    print("e) Press e to exit the program")
    print("or")
    print("q) Press q to exit the program")
    print("j) Press j to list all genres")
    print("a) Press a to list all albums")
    print(u'\u2500'* 30)

if __name__ == "__main__":
    main()
