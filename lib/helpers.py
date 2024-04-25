# lib/helpers.py
from models.genres import Genres
from models.albums import Albums


def exit_program():
    print("Goodbye!")
    exit()

# Genres helper functions
def list_all_genres():
    genres = Genres.get_all()
    for genre in genres:
        print(genre)

def create_genre():
    name = input("Add another music genre: ")
    try:
        genre = Genres.create(name)
        print(f'Added {genre}')
    except Exception as exc:
        print("Encountered an error adding genre ", exc)

def update_genre():
    coll = input("Enter the genre's name: ").capitalize()
    if genre := Genres.find_by_name(coll):
        try:
            name = input("Enter the updated genre name: ")
            if len(name) == 0:
                print(f'No new name was entered, so there is no change to make to {genre}')
            else:
                print(f'Updating {genre}')
                genre.name = name
            genre.update()
            print(f'{genre} updated')
        except Exception as exc:
            print("There was an error updating the genre: ", exc)
    else:
        print(f'Genre {coll} was not found - please check your spelling and try again')

def delete_genre():
    name = input("Enter the name of the genre: ").capitalize()
    if name := Genres.find_by_name(name):
        name.delete()
        print(f'Genre {name} deleted')
    else:
        print(f'Genre {name} not found - please check spelling and try again')

# Albums helper functions
def list_all_albums():
    albums = Albums.get_all()
    for album in albums:
        print(album)

def create_album():
    title = input("Add the title of another music album: ")
    artist = input("Add the artist for that album: ")
    year = input("Add the year of the album's initial release: ")
    genre = input("Add the genre from the available genres to categorize the album.  If the best one is not listed, please add the genre to the list")
    try:
        album = Albums.create(title, artist, year)
        print(f'Added {album}')
    except Exception as exc:
        print("Encountered an error adding album ", exc)

def update_album():
    coll = input("Enter the album's name: ")
    if album := Albums.find_by_title(coll):
        try:
            title = input("Enter the updated album title: ")
            artist = input("Enter the updated artist name: ")
            year = input("Enter the updated album release year: ")
            genre = input("Enter the updated genre from the list of genres: ")
            if len(title):
                print(f'No new name was entered, so there is no change to make to {title} ')
            elif len(artist):
                print(f'No new name was entered, so there is no change to make to {artist} ')
            elif len(str(year)):
                print(f'No new year was entered, so there is no change to make to {album} ')
            elif len(genre):
                print(f'No new name was entered, so there is no change to make to {album} ')
            else:
                print(f'Updating {album}')
                album.title = title
                album.artist = artist
                album.year = year
                album.genre = genre
            album.update()
            print(f'{album} updated')
        except Exception as exc:
            print("There was an error updating the album: ", exc)
    else:
        print(f'album {coll} was not found - please check your spelling and try again')
        
def delete_album():
    title = input("Enter the title of the album: ")
    if album := Albums.find_by_title(title):
        album.delete()
        print(f'Genre {album} deleted')
    else:
        print(f'Album {album} not found - please check spelling and try again')
        
def all_albums_from_genre():
    # all_albums = list_all_albums()
    for album in list_all_albums():
        breakpoint()
