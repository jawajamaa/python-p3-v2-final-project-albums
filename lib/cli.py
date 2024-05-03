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
    update_album_by_genre,
    delete_album_by_genre,
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
                albums_of_genre_menu(val, show_albums_by_genre(val.name))

        if choice == 'b':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  


def albums_of_genre_menu(selected_genre, albums):
    while True:
        print(u'\u2500'* 80)
        print(u'\u2500'* 80)
        print("Albums of a Specific Genre Menu")
        print(u'\u2500'* 80) 
        print(space20(len("Artist")),"Album Title",space30(len("Album Title")),"Artist",space10(len("Artist")), "Year",space10(len("Year")), "Category",space10(len("Category")))
        print(u'\u2500'* 80)
        for i, album in enumerate(albums, start = 1):   
            print(f'''
                {i}{" - "}{album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}
            ''')  
        print("""
            Please select an option from below
              or a number of an album from above
            
            a   -   Add albums in genre
            b   -   Back to main menu
            q   -   Exit the program
            """)
        choice = input(">")
        for i, album in enumerate(albums, start = 1):   
            if choice == str(i):
                selected_album_menu(album)

        if choice == 'a':
            create_album_by_genre(selected_genre)
        elif choice == 'b':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  
    
def selected_album_menu(album):
    while True:
        # breakpoint()
        print(u'\u2500'* 80)
        print(u'\u2500'* 80)
        print("Selected Album Menu")
        print(u'\u2500'* 80) 
        print(space20(len("Artist")),"Album Title",space30(len("Album Title")),"Artist",space10(len("Artist")), "Year",space10(len("Year")), "Category",space10(len("Category")))
        print(u'\u2500'* 80)
   
        print(f'''
                {album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}
            ''')  
        print("""
            Please select an option
            
            u   -   Update album
            d   -   Delete album
            b   -   Back to main menu
            q   -   Exit the program
            """)
        
        choice = input(">")
        if choice == 'u':
            update_album_by_genre(album)
        elif choice == 'd':
            delete_album_by_genre(album)
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
        print("Artist Menu")
        print(space20(len("Artist")),"Artists")
        all_albums = list_all_albums()
        for i, album in enumerate(all_albums, start = 1):
            print(f'{i}{"   -   "}{album.artist}')
            # make list comp to also drop any dupe artists?
        print("""
            a  -   Add new Album
            u  -   Update existing Album
            d  -   Delete existing Album
            b  -   Back to main menu
            q  -   Exit the program
            """)
        print('\u2500'* 60)
        print('\u2500'* 60)

        choice = input(">")

        for i, album in enumerate(all_albums, start = 1):
            if choice == int(i):
                breakpoint()
        if choice == 'l':
            list_all_albums()
        elif choice == 'a':
            pass
            # create_album_by_artist()? not created yet
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
            albums = list_all_albums()

            print(space20(len("Year")),"Album Title",space30(len("Album Title")),"Artist",space10(len("Artist")), "Year",space10(len("Year")), "Category",space10(len("Category")))
            for i, album in enumerate(albums, start=1):   
                print(f'''
                    {i}{""    -   ""}{album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}{space10(len(album.genre.name))}
                ''')
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
