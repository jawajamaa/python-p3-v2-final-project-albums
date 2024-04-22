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



# Albums helper functions
def list_all_albums():
    albums = Albums.get_all()
    for album in albums:
        print(album)
