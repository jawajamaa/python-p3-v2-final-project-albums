# lib/cli.py

from helpers import (
    exit_program,
    list_all_albums,
    create_album,
    update_album,
    delete_album,
    show_albums_by_genre,
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
            s   -   Albums by genre
            q   -   Exit the program
            """)
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)

        choice = input(">")
        if choice == 'g':
            genre_menu()
        elif choice == 'a':
            album_menu()
        elif choice == 's':
            albums_by_genre_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")


def albums_by_genre_menu():
    while True:
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)
        print("Albums by Genre Menu")
        print("""
            1  -   Blues
            2  -   Drum'n'Bass
            3  -   House
            4  -   Jazz
            5  -   Metal
            6  -   Nu-Metal
            7  -   Psychedelic Soul
            8  -   Punk
            9  -   Rock
            10 -   Soul-Jazz
            11 -   Techno
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
        if choice == "1" :
            show_albums_by_genre("Blues")
        elif choice == "2" :
            show_albums_by_genre("Drum'n'Bass")
        elif choice == "3" :
            show_albums_by_genre("House")
        elif choice == "4" :
            show_albums_by_genre("Jazz")
        elif choice == "5" :
            show_albums_by_genre("Metal")
        elif choice == "6" :
            show_albums_by_genre("Nu-Metal")
        elif choice == "7" :
            show_albums_by_genre("Psychedelic Soul")
        elif choice == "8" :
            show_albums_by_genre("Punk")
        elif choice == "9" :
            show_albums_by_genre("Rock")
        elif choice == "10" :
            show_albums_by_genre("Soul-Jazz")
        elif choice == "11" :
            show_albums_by_genre("Techno")
        elif choice == 'l':
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
