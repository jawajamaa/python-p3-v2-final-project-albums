# lib/cli.py

from helpers import (
    exit_program,
    list_all_albums,
    create_album,
    update_album,
    delete_album,
    list_all_genres,
    create_genre,
    update_genre,
    delete_genre
)


def main():
    print("Welcome to your digital guide for your tangible music collection!")
    main_menu()
    
    choice = ""
    choice = input(">")
#     while choice != "q":
#         genre_choice = ""
#         album_choice = ""
#         if choice == "a":
#             list_all_albums()
#             album_menu()
#             album_choice = input(">")
#             while album_choice != "q" or album_choice != "b": 
#                 if album_choice == "d":
#                     create_album()
#                 if album_choice == "e":
#                     update_album()
#                 if album_choice == "r":
#                     delete_album()
# # choice b creates recursion of the main menu populating again and again... 
#                 if album_choice == "b":
#                     main_menu()
#                 if album_choice == "q":
#                     exit_program()
#         if choice == "j":
#             list_all_genres()
#             genre_menu()
#             genre_choice = input(">")
#             while genre_choice != "q" or genre_choice != "b":
#                 if genre_choice == "k":
#                     create_genre()
# # can add new genre and works but only prompt is to add another new genre and can't exit without control+c 
#                 if genre_choice == "u":
#                     update_genre()
#                 if genre_choice == "l":
#                     delete_genre()
# # choice b creates recursion of the main menu populating again and again... 
#                 if genre_choice == "b":
#                     main_menu()
#                 if genre_choice == "q":
#                     exit_program()
#         if choice == "q":
#             exit_program()
#         else:
#             print("Please choose one of the listed options")

def main_menu():
    while True:
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)
        print("Main Menu")
        print("""
            Please select an option
            
            g   -   Admin genres
            a   -   Admin albums
            q   -   Exit the program
            """)
        print(u'\u2500'* 60)
        print(u'\u2500'* 60)

        choice = input(">")
        if choice == 'g':
            genre_menu()
        elif choice == 'a':
            album_menu()
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")


# make album menu match genre menu
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
            return
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
            return
        elif choice == 'q':
            exit_program()
        else:
            print("Please choose one of the listed options")        


if __name__ == "__main__":
    main()
