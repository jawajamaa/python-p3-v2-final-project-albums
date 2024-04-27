# lib/helpers.py
from models.genres import Genre
from models.albums import Album


def exit_program():
    print("Goodbye!")
    exit()

# Genres helper functions
def list_all_genres():
    genres = Genre.get_all()
    print(u'\u2500'* 60)
    for genre in genres:
        print(genre.name)

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

# Albums helper functions
def list_all_albums():
    albums = Album.get_all()
    print("Album Title\t", "Artist\t", "Year\t", "Category\t")
    for album in albums:  
        # breakpoint()  
        print(f'''
            {album.title}{space30(len(album.title))}{album.artist}{space20(len(album.artist))}{album.year}{space10(len(str(album.year)))}{album.genre.name}{space10(len(album.genre.name))}
        ''')
    # reformat album

def space30(num):
    spaces = int((30 - num))
    return(spaces*" ")

def space20(num):
    spaces = int((20 - num))
    return(spaces*" ")

def space10(num):
    spaces = int((10 - num))
    return(spaces*" ")

def create_album():
    title = input("Add the title of another music album: ")
    artist = input("Add the artist for that album: ")
    year = input("Add the year of the album's initial release: ")
    genre_name = input("Add the genre from the available genres to categorize the album.  If the best one is not listed, please add the genre to the list: ")
    if genre := Genre.find_by_name(genre_name):
        try:
            album = Album.create(title, artist, year, genre)
            print(f'Added {title}')
        except Exception as exc:
            print("Encountered an error adding album ", exc)
    else:
        print("invalid genre {genre_name}")

def update_album():
    coll = input("Enter the album's title: ")
    if album := Album.find_by_title(coll):
        print(album)
        try:

            title = input("Enter the updated album title: ")
            if len(title) <= 0:
                print(f'No new name was entered, so there is no change to make to {title} ')
            else:
                print(f'Updating {title}')
                album.title = title

            artist = input("Enter the updated artist name: ")
            if len(artist) <= 0:
                print(f'No new or updated name was entered, so there is no change to make to {artist} ')
            else:
                print(f'Updating {title}\'s {artist}')
                album.artist = artist

            year = input("Enter the updated album release year: ")
            if len(str(year)) <= 0:
                print(f'No new year was entered, so there is no change to make to {title} ')
            elif len(str(year)) != 4:
                print(f'The year entered needs to be 4 digits, so there is no change that can be made to {title}\'s release year ')
            # elif 0 < len(str(year)) <= 3:
            #     print(f'The year entered needs to be 4 digits, so there is no change that can be made to {title}\'s release year ')
            else:
                print(f'Updating {title}\'s release year of {year}')
                album.year = year
            
            genre = input("Enter the updated genre from the list of genres: ")
            if len(genre) <= 0:
                print(f'No new name was entered, so there is no change to make to {genre} ')
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
        
# def update_album():
#     coll = input("Enter the album's title: ")
#     if album := Album.find_by_title(coll):
#         try:
#             title = input("Enter the updated album title: ")
#             artist = input("Enter the updated artist name: ")
#             year = input("Enter the updated album release year: ")
#             genre = input("Enter the updated genre from the list of genres: ")
#             if len(title):
#                 breakpoint()
#                 print(f'No new name was entered, so there is no change to make to {title} ')
#             elif len(artist):
#                 print(f'No new name was entered, so there is no change to make to {artist} ')
#             elif len(str(year)):
#                 print(f'No new year was entered, so there is no change to make to {album} ')
#             elif len(genre):
#                 print(f'No new name was entered, so there is no change to make to {album} ')
#             else:
#                 print(f'Updating {album}')
#                 album.title = title
#                 album.artist = artist
#                 album.year = year
#                 album.genre = genre
#             album.update()
#             print(f'{album} updated')
#         except Exception as exc:
#             print("There was an error updating the album: ", exc)
#     else:
#         print(f'album {coll} was not found - please check your spelling and try again')

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
