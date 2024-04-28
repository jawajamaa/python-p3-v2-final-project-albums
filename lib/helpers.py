# lib/helpers.py
from models.genre import Genre
from models.album import Album
import copy

def exit_program():
    print("Goodbye!")
    exit()

# Genres helper functions
def list_all_genres():
    genres = Genre.get_all()
    print(f'{space20(len("Categories"))}Categories')
    print(u'\u2500'* 60)
    for genre in genres:
        print(f'{space20(len(genre.name))}{genre.name}')

def create_genre():
    name = input("Add another music genre: ")
    try:
        genre = Genre.create(name)
        print(f'Added {genre}')
    except Exception as exc:
        print("Encountered an error adding genre ", exc)

def update_genre():
    coll = input("Enter the genre's name: ")
    if genre := Genre.find_by_name(coll):
        try:
            name = input("Enter the updated genre name: ")
            if len(name) == 0:
                print(f'No new name was entered, so there is no change to make to {genre}')
            else:
                print(f'Updating {genre}')
                genre = Genre(name, genre.id)
                genre.update()
                print(f'{genre} updated')
        except Exception as exc:
            print("There was an error updating the genre: ", exc)
    else:
        print(f'Genre {coll} was not found - please check your spelling and try again')

def delete_genre():
    name = input("Enter the name of the genre: ")
    if genre := Genre.find_by_name(name):
        genre.delete()
        print(f'Genre {name} deleted')
    else:
        print(f'Genre {name} not found - please check spelling and try again')

# formatting in cli - add spaces
def space30(num):
    spaces = int((30 - num))
    return(spaces*" ")

def space20(num):
    spaces = int((20 - num))
    return(spaces*" ")

def space10(num):
    spaces = int((10 - num))
    return(spaces*" ")

# Albums helper functions
def list_all_albums():
    albums = Album.get_all()
    print("Album Title\t", "Artist\t", "Year\t", "Category\t")
    for album in albums:   
        print(f'''
            {album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}{space10(len(album.genre.name))}
        ''')


def create_album():
    
    def create_title():
        title = input("Add the title of another music album: ")
        if len(title) < 1:
            print("Title field must not be empty; for self-titled albums please enter the artist's name for both fields.")
            create_title()
        else:
            return title

    def create_artist():
        artist = input("Add the artist for that album: ")
        if len(artist) < 1:
            print("Artist field must not be empty; for self-titled albums please enter the artist's name for both fields.")
            create_artist()
        else:
            return artist

    def create_year():
        year = input("Add the year of the album's initial release: ")
        if type(year) != int:
            print(type(year) != int)
            if len(str(year)) != 4:
                print(len(str(year)) != 4)
                print("The year of release must be an integer 4 digits in length")
                create_year()
        else:
            return year
            # return int(year)

    def create_genre():
        list_all_genres()        
        genre_name = input("Add the genre from the available genres to categorize the album.  If the best one is not listed, please add the genre to the list: ")
        if genre := Genre.find_by_name(genre_name):
            return genre
        else:
            print(f"invalid genre {genre_name}")

    try:
        album = Album.create(create_title(), create_artist(), create_year(), create_genre())
        print(f'Added {album.title}')
    except Exception as exc:
        print("Encountered an error adding album ", exc)


def update_album():
    coll = input("Enter the album's title: ")
    if album := Album.find_by_title(coll):
        album_dupe = copy.deepcopy(album)
        # make deep copy of retrieved album and use that information for the cases where the attribute (ie: artist, title, year etc.) doesn't need to be updated
        try:

            title = input("Enter the updated album title: ")
            if len(title) <= 0:
                print(f'No new name was entered, so there is no change to make...')
                title = album_dupe.title
            else:
                print(f'Updating {title}')
                album.title = title

            artist = input("Enter the updated artist name: ")
            if len(artist) <= 0:
                print(f'No new or updated name was entered, so there is no change to make...')
                artist = album_dupe.artist
            else:
                print(f'Updating {title}\'s {artist}')
                album.artist = artist

            year = input("Enter the updated album release year: ")
            if len(str(year)) <= 0:
                print(f'No new year was entered, so there is no change to make... ')
                year = album_dupe.year
            elif len(str(year)) != 4:
                print(f'The year entered needs to be 4 digits, so there is no change that can be made to the album\'s release year ')
                year = album_dupe.year
            else:
                print(f'Updating {title}\'s release year of {year}')
                album.year = year
            
            genre = input("Enter the updated genre from the list of genres: ")
            if len(genre) <= 0:
                print(f'No new name was entered, so there is no change to make...')
                genre = album_dupe.genre
            else:
                print(f'Updating {genre}')
                genre = Genre.find_by_name(genre)

            album = Album(title, artist, year, genre, album.id )
            album.update()
            print(f'{artist}\'s {genre} album, {title} first released in {year} updated')
        except Exception as exc:
            print("There was an error updating the album: ", exc)
    else:
        print(f'album {coll} was not found - please check your spelling and try again')

def delete_album():
    title = input("Enter the title of the album: ")
    if album := Album.find_by_title(title):
        album.delete()
        print(f'Genre {album} deleted')
    else:
        print(f'Album {album} not found - please check spelling and try again')

def all_albums_from_genre():
    # all_albums = list_all_albums()
    for album in list_all_albums():
        breakpoint()
