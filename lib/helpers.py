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


# Albums helper functions
def list_all_albums():
    albums = Albums.get_all()
    for album in albums:
        print(album)

def create_album():
    name = input("Add another music album: ")
    try:
        album = Albums.create(name)
        print(f'Added {album}')
    except Exception as exc:
        print("Encountered an error adding album ", exc)

def update_album():
    coll = input("Enter the album's name: ").capitalize()
    if album := Albums.find_by_name(coll):
        try:
            name = input("Enter the updated album name: ")
            if len(name) == 0:
                print(f'No new name was entered, so there is no change to make to {album}')
            else:
                print(f'Updating {album}')
                album.name = name
            album.update()
            print(f'{album} updated')
        except Exception as exc:
            print("There was an error updating the album: ", exc)
    else:
        print(f'album {coll} was not found - please check your spelling and try again')
        
def all_albums_from_genre():
    # all_albums = list_all_albums()
    for album in list_all_albums():
        breakpoint()
