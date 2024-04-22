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
    print("Please select an option")
    print("Press e or q to exit the program")
    print("Press j to list all genres")
    print("Press a to list all albums")
    print("Some pointless function")

if __name__ == "__main__":
    main()
