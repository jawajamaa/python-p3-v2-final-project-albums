# lib/cli.py

from helpers import (
    exit_program,
    list_all_albums,
    create_album,
    update_album,
    list_all_genres,
    create_genre,
    update_genre
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
            choice = input(">")
            while album_choice != "q" or album_choice != "b": 
                album_menu()
                if album_choice == "d":
                    create_album()
                if album_choice == "e":
                    update_album()
                if album_choice == "b":
                    main_menu()
                if album_choice == "q":
                    exit_program()
        if choice == "j":
            list_all_genres()
            genre_choice = ""
            choice = input(">")
            while genre_choice != "q" or genre_choice != "b":
                genre_menu()
                if genre_choice == "k":
                    create_genre()
                if genre_choice == "l":
                    update_genre()
                if genre_choice == "b":
                    main_menu()
                if genre_choice == "q":
                    exit_program()
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
    print("d)   Add new album")
    print("e)   Update existing album")
    print("b)   Back to main menu")
    print("q)   Exit the program")
    print(u'\u2500'* 30)

def genre_menu():
    print(u'\u2500'* 30)
    print("Genre Menu")
    print("Please select an option")
    print("")
    print("k)   Add new genre")
    print("l)   Update existing genre")
    print("b)   Back to main menu")
    print("q)   Exit the program")
    print(u'\u2500'* 30)

if __name__ == "__main__":
    main()
