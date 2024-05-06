# lib/cli.py
from models.genre import Genre
from helpers import (
    exit_program,
    list_all_albums,
    create_album,
    update_album,
    delete_album,
    list_all_albums_by_artist,
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
    space10,
    line,
    final_frontier
)

def headings20():
    print(space20(len("Year")),"Album Title",space30(len("Artist")),"Artist",space20(len("spacers")), "Year",space10(len("Artistry")), "Category",space10(len("Category")))

def headings30():
    print(space30(len("Year")),"Album Title",space30(len("Artist")),"Artist",space20(len("spacers")), "Year",space10(len("Artistry")), "Category",space10(len("Category")))

def main():
    line()
    print("Welcome to your digital guide for your tangible music collection!")
    main_menu()


def main_menu():
    while True:
        line()
        line()
        print("Main Menu")
        print("""
            Please select an option
            
            d   -   Display all artists
            s   -   Show albums by genre
            q   -   Exit the program
            """)
        line()
        line()

        choice = input(">")
        if choice == 'g':
            genre_menu()
        elif choice == 'a':
            album_menu()
        elif choice == 'd':
            list_all_artists_menu()
        elif choice == 's':
            albums_by_genre_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")


# below is to refactor listing genres out so it can be called from helpers line 109 and below line 88
def list_of_genres():
    print(f'{space10(len("Choice"))}Choose from categories')  
    print("") 
    for i, val in enumerate(Genre.get_all(), start = 1):  
        print(f'        {i}    -    {space10(len(val.name))}{val. name}')
    print("""
        m  -   Back to main menu
        q  -   Exit the program
        """)
    line()
    line()  
 

def albums_by_genre_menu():
    while True:
        line()
        line()
        print("Albums by Genre Menu")
        line() 
        list_of_genres() 

        choice = input(">")
        for i, val in enumerate(Genre.get_all(), start = 1):  
            if choice == str(i):
                albums_of_genre_menu(val, show_albums_by_genre(val.name))

        if choice == 'm':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  


def albums_of_genre_menu(selected_genre, albums):
    while True:
        line()
        line()
        print("Albums of a Specific Genre Menu")
        line() 
        headings20()
        line()
        if len(albums):
            for i, album in enumerate(albums, start = 1):   
                print(f'''
                    {i}{" - "}{album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}
                ''') 
        else:
            print("There are currently no albums of this genre currently stored in the database") 
        print("""
            Please select an option from below
              or a number of an album from above
            
            a   -   Add albums in genre
            4d  -   Delete album in genre (eg. this would delete album #4 )
            m   -   Back to main menu
            b   -   Back to Albums by Genre Menu
            q   -   Exit the program
            """)
        choice = input(">")
        for i, album in enumerate(albums, start = 1):   
            if choice == str(i):
                selected_album_menu(album)
            elif choice == str(i)+"d":
                print(f'Are you sure you would like to delete {album.title}?')
                delete_choice = input(">")
                if delete_choice == "Y" or delete_choice == "y":
                    delete_album_by_genre(album)
                    albums.remove(album)
                    albums_of_genre_menu(selected_genre, albums)
                else:
                    albums_of_genre_menu(selected_genre, albums)

        if choice == 'a':
            new_album = create_album_by_genre(selected_genre)
            if new_album is not None: 
                albums.append(new_album)
                albums_of_genre_menu(selected_genre, albums)
        elif choice == 'm':
            main_menu()
        elif choice == 'b':
            albums_by_genre_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  
    

def selected_album_menu(album):
    while True:
        line()
        line()
        print("Selected Album Menu")
        line() 
        headings20()
        line()
   
        print(f'''
                {album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}
            ''')  
        print("""
            Please select an option
            
            u   -   Update album
            d   -   Delete album
            m   -   Back to main menu
            q   -   Exit the program
            """)
        
        choice = input(">")
        if choice == 'u':
            update_album_by_genre(album)
        elif choice == 'd':
            delete_album_by_genre(album)
        elif choice == 'm':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options") 


def list_all_artists_menu():
    while True:
        line()
        line()
        print("All Artists Menu")
        final_frontier()
        print(space20(len("Artist")),"Artists")
        all_albums = list_all_albums()
        all_artists = sorted(set(album.artist for album in all_albums if album.artist))

        for i, artist in enumerate(all_artists, start = 1):
            print(f'{i}{"   -   "}{artist}')

        print("""
              Please select an option from below or an artist from the list to 
              view, update or delete their albums

            l   -   List all Albums  
            m   -   Back to main menu
            q   -   Exit the program
            """)
        line()
        line()

        choice = input(">")

        for i, artist in enumerate(all_artists, start = 1):
            if choice == str(i):
                show_albums_by_artist_menu(list_all_albums_by_artist(artist))

        if choice == 'l':
            albums = list_all_albums()

            headings20()
            for i, album in enumerate(albums, start=1):   
                print(f'''
                    {i}{"    -   "}{album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}{space10(len(album.genre.name))}
                ''')

        elif choice == 'm':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  


def show_albums_by_artist_menu(albums_of_artist):
    while True:
        line()
        line()
        print("Selected Artists's Albums Menu")
        line() 
        headings20()
        line()
        for i, album in enumerate(albums_of_artist, start = 1):
            print(f'''
                {i}{"   -   "}{album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}
            ''')  
        print("""
            Please select an option or choose an album to modify
            
            a   -   Add an album by current artist
            b   -   Back to previous menu
            m   -   Back to main menu
            q   -   Exit the program
            """)
        
        choice = input(">")

        for i, album in enumerate(albums_of_artist, start = 1):
            if choice == str(i):
                selected_album_menu(album)

        if choice == 'a':
            artist = albums_of_artist[0].artist
            create_album(artist)
        elif choice == 'b':
            list_all_artists_menu()
        elif choice == 'm':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options") 


def album_menu():
    while True:
        line()
        line()
        print("Album Menu")
        print("""
            l  -   List all Albums
            a  -   Add new Album
            u  -   Update existing Album
            d  -   Delete existing Album
            m  -   Back to main menu
            q  -   Exit the program
            """)
        line()
        line()

        choice = input(">")

        if choice == 'l':
            albums = list_all_albums()

            headings20()
            for i, album in enumerate(albums, start=1):   
                print(f'''
                    {i}{"    -   "}{album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}{space10(len(album.genre.name))}
                ''')
        elif choice == 'a':
            create_album()
        elif choice == 'u':
            update_album()
        elif choice == 'd':
            delete_album()
        elif choice == 'm':
            main_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")  


def genre_menu():
    while True:
        line()
        line()
        print("Genre Menu")
        print("""
            l  -   List all genres
            a  -   Add new genre
            u  -   Update existing genre
            d  -   Delete existing genre
            m  -   Back to main menu
            q  -   Exit the program
            """)
        line()
        line()

        choice = input(">")
        if choice == 'l':
            list_all_genres()
        elif choice == 'a':
            create_genre()
        elif choice == 'u':
            update_genre()
        elif choice == 'd':
            delete_genre()
        elif choice == 'm':
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
