# lib/cli.py

from helpers import (
    exit_program,
    list_all_albums,
    list_all_genres
)


def main():
    main_menu()
    print("Welcome to your digital guide for your tangible music collection!")
    choice = ""
    choice = input(">")
    while choice != "q":
        if choice == "a":
            list_all_albums()
            album_choice = ""
            while album_choice != "q" or album_choice != "b": 
                album_menu()
                if album_choice == "d":
                    
        if choice == "j":
            list_all_genres()
            genre_menu()
        if choice == "q":
            exit_program()
        else:
            print("Please choose one of the listed options")

def main_menu():
    print(u'\u2500'* 30)
    print("Main Menu")
    print("""
        Please select an option
          
        j   -   List all genres
        a   -   List all albums
        q   -   Exit the program
          """)
    print(u'\u2500'* 30)

def album_menu():
    print(u'\u2500'* 30)
    print("Album Menu")
    print("Please select an option")
    print("")
    print("This is the album menu")
    print("b)   Back to main menu")
    print("q)   Exit the program")
    print(u'\u2500'* 30)

def genre_menu():
    genre_choice = ""
    genre_choice = input(">")
    print(u'\u2500'* 30)
    print("Album Menu")
    print("Please select an option")
    print("")
    print("This is the genre menu")
    print("b)   Back to main menu")
    print("q)   Exit the program")
    print(u'\u2500'* 30)

if __name__ == "__main__":
    main()
