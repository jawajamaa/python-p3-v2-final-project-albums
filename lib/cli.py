# lib/cli.py

from helpers import (
    exit_program,
    list_all_albums,
    create_album,
    update_album,
    delete_album,
    list_all_genres,
    create_genre,
    update_genre,
    delete_genre
)


def main():
    print("Welcome to your digital guide for your tangible music collection!")
    main_menu()


def main_menu():
    while True:
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)
        print("Main Menu")
        print("""
            Please select an option
            
            g   -   Admin genres
            a   -   Admin albums
            q   -   Exit the program
            """)
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)

        choice = input(">")
        if choice == 'g':
            genre_menu()
        elif choice == 'a':
            album_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")


def album_menu():
    while True:
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)
        print("Album Menu")
        print("""
            l  -   List all Albums
            a  -   Add new Album
            u  -   Update existing Album
            d  -   Delete existing Album
            b  -   Back to main menu
            q  -   Exit the program
            """)
        print('\u2500'* 60)
        print('\u2500'* 60)

        choice = input(">")
        if choice == 'l':
            list_all_albums()
        elif choice == 'a':
            create_album()
        elif choice == 'u':
            update_album()
        elif choice == 'd':
            delete_album()
        elif choice == 'b':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  


def genre_menu():
    while True:
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)
        print("Genre Menu")
        print("""
            l  -   List all genres
            a  -   Add new genre
            u  -   Update existing genre
            d  -   Delete existing genre
            b  -   Back to main menu
            q  -   Exit the program
            """)
        print('\u2500'* 60)
        print('\u2500'* 60)

        choice = input(">")
        if choice == 'l':
            list_all_genres()
        elif choice == 'a':
            create_genre()
        elif choice == 'u':
            update_genre()
        elif choice == 'd':
            delete_genre()
        elif choice == 'b':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")        


if __name__ == "__main__":
    main()
