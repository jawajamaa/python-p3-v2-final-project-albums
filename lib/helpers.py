# lib/helpers.py
from models.genre import Genre
from models.album import Album
import copy

def exit_program():
    print("Goodbye!")
    exit()

# Genres helper functions
def list_all_genres():
    return Genre.get_all()

def create_genre():
    name = input("Add another music genre: ")
    try:
        genre = Genre.create(name)
        print(f'Added {genre.name}')
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
                print(f'Updating {genre.name}')
                genre = Genre(name, genre.id)
                genre.update()
                print(f'{genre.name} updated')
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

# formatting in cli - blank line for readability
def final_frontier():
    print("")

# formatting in cli - horizontal line for readability
def line():
    print(u'\u2500'* 100)

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
    return Album.get_all()

def list_all_genres_of_albums():
    return Album.genres()

def create_album(artist = None):

    def create_title():
        title = input("Add the title of another music album: ")
        if len(title) < 1:
            print("Title field must not be empty; for self-titled albums please enter the artist's name for both fields.")
            create_title()
        else:
            return title

    def create_artist(artist = None):
        if artist == None:
            artist = input("Add the artist for that album: ")
            if len(artist) < 1:
                print("Artist field must not be empty; for self-titled albums please enter the artist's name for both fields.")
                create_artist()

        return artist

    def create_year():
        year = input("Add the year of the album's initial release: ")
        if len(year) == 4 and year.isdigit():
                return year
        else:
            print("The year of release must be an integer 4 digits in length")
            return create_year()
# above function was refactored courtesy ChatGPT using isdigit() and return create_year() when I had been checking type == int and invoking create_year() recursively if invalid inputs

    def create_genre():
        from cli import list_of_genres
        list_of_genres()
        choice = input(">")
        
        for i, val in enumerate(Genre.get_all(), start = 1):  
            if choice == str(i):
                genre_name = val.name
    
        if genre := Genre.find_by_name(genre_name):
            return genre
        else:
            print(f"My apologies, {genre_name} is an invalid genre")

    try:
        album = Album.create(create_title(), create_artist(artist), create_year(), create_genre())
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
                print(f'Updating {genre.name}')
                genre = Genre.find_by_name(genre)

            album = Album(title, artist, year, genre, album.id )
            album.update()
            print(f'{artist}\'s album, {title} first released in {year} and classified as {genre.name} updated')
        except Exception as exc:
            print("There was an error updating the album: ", exc)
    else:
        print(f'album {coll} was not found - please check your spelling and try again')

def delete_album():
    title = input("Enter the title of the album: ")
    if album := Album.find_by_title(title):
        album.delete()
        print(f'Album {album.title} deleted')
    else:
        print(f'Album {album} not found - please check spelling and try again')

def show_albums_by_genre(selected_genre):
    return Album.find_by_genre(selected_genre)

def list_all_albums_by_artist(selected_artist):
    return Album.find_by_artist(selected_artist)

def create_album_by_genre(selected_genre):

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
        if len(year) == 4 and year.isdigit():
                return year
        else:
            print("The year of release must be an integer 4 digits in length")
            return create_year()
# above function was refactored courtesy ChatGPT using isdigit() and return create_year() when I had been checking type == int and invoking create_year() recursively if invalid inputs

    try:
        album = Album.create(create_title(), create_artist(), create_year(), selected_genre)
        print(f'Added {album.title}')
        return album
    except Exception as exc:
        print("Encountered an error adding album ", exc)
        return None

def update_album_by_genre(album):
        album_dupe = copy.deepcopy(album)

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

            updated_album = Album(title, artist, year, album.genre, album.id )
            updated_album.update()
            print(f'{artist}\'s album, {title} first released in {year} and classified as {album.genre.name} has been updated')
        except Exception as exc:
            print("There was an error updating the album: ", exc)


def delete_album_by_genre(album):
    album.delete()
    print(f'Album {album.title} deleted')
