# lib/cli.py
from models.genre import Genre
from helpers import (
    exit_program,
    list_all_albums,
    create_album,
    update_album,
    delete_album,
    show_albums_by_genre,
    create_album_by_genre,
    list_all_genres,
    create_genre,
    update_genre,
    delete_genre,
    space30,
    space20,
    space10
)

def main():
    print(u'\u2500'* 80)
    print("Welcome to your digital guide for your tangible music collection!")
    main_menu()


def main_menu():
    while True:
        print(u'\u2500'* 80)
        print(u'\u2500'* 80)
        print("Main Menu")
        print("""
            Please select an option
            
            d   -   Display albums by artist
            s   -   Show albums by genre
            q   -   Exit the program
            """)
        print(u'\u2500'* 80)
        print(u'\u2500'* 80)

        choice = input(">")
        if choice == 'g':
            genre_menu()
        elif choice == 'a':
            album_menu()
        elif choice == 'd':
            albums_by_artist_menu()
        elif choice == 's':
            albums_by_genre_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")


def albums_by_genre_menu():
    while True:
        print(u'\u2500'* 80)
        print(u'\u2500'* 80)
        print("Albums by Genre Menu")
        # list_all_genres()
        print(u'\u2500'* 80)  
        print(f'{space10(len("Choice"))}Choose from categories')  
        print("") 
        for i, val in enumerate(Genre.get_all(), start = 1):  
            print(f'        {i}    -    {space10(len(val.name))}{val. name}')
        print("""

            b  -   Back to main menu
            q  -   Exit the program
            """)
        print(u'\u2500'* 80)
        print(u'\u2500'* 80)

        choice = input(">")
        for i, val in enumerate(Genre.get_all(), start = 1):  
            if choice == str(i):
                show_albums_by_genre(val.name)
                albums_of_genre_menu(val)

        if choice == 'b':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  


def albums_of_genre_menu(selected_genre):
    while True:
        print(u'\u2500'* 80)
        print(u'\u2500'* 80)
        print("Albums of a Specific Genre Menu")
        print(u'\u2500'* 80)  
        print(f'{space10(len("Choice"))}Please select an option')  
        print("""
            Please select an option
            
            a   -   Add albums in genre
            u   -   Update albums in genre
            d   -   Delete albums in genre
            b   -   Back to main menu
            q   -   Exit the program
            """)
        choice = input(">")
        if choice == 'a':
            create_album_by_genre(selected_genre)
        elif choice == 'u':
            update_album_by_genre(selected_genre)
        elif choice == 'd':
            delete_album()
        elif choice == 'b':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  
    


def albums_by_artist_menu():
    while True:
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)
        print("Albums by Artist Menu")
        print("""
            1  -   Artist1
            2  -   Artist2
            3  -   Artist3
            4  -   Artist4
            5  -   Artist5
            6  -   Artist6
            7  -   Artist7
            8  -   Artist8
            9  -   Artist9
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
            create_album_by_genre(selected_genre)
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


# removed from main_menu() at around ln 30
            # g   -   Admin genres
            # a   -   Admin albums
