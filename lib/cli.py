# lib/cli.py

from helpers import (
    exit_program,
    list_all_albums,
    list_all_genres
)


def main():
    choice = ""
    main_menu()
    choice = input(">")
    while choice != "q":
        if choice == "q":
            exit_program()
        if choice == "a":
            list_all_albums()
            album_menu()
        if choice == "j":
            list_all_genres()
            genre_menu()
        else:
            print("Please choose one of the listed options")

def main_menu():
    print(u'\u2500'* 30)
    print("""
        Please select an option
          
        j   -   List all genres
        a   -   List all albums
        q   -   Exit the program
          """)
    print(u'\u2500'* 30)

def album_menu():
    print(u'\u2500'* 30)
    print("Please select an option")
    print("")
    print("This is the album menu")
    print("b)   Back to main menu")
    print("q)   Exit the program")
    print(u'\u2500'* 30)

def genre_menu():
    print(u'\u2500'* 30)
    print("Please select an option")
    print("")
    print("This is the genre menu")
    print("b)   Back to main menu")
    print("q)   Exit the program")
    print(u'\u2500'* 30)

if __name__ == "__main__":
    main()
