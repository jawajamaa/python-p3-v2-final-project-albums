# timothy ryon Phase 3 CLI ORM project - albums

This is a command line Python project, but the tables in the database can also be viewed by any database program that will work with SQLite3.  My one to many relationship is one genre can be related to many albums of that genre.  The directory structure is as follows below.

Directory structure:

```console
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── genre.py
    |   └── album.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```

## CRUD operations

The seed.py file contains 10 genres and 18 albums for the intial creation of the tables, but as it stands currently, the database has already been seeded and more albums have been added.  Once that is created, one can navigate into the main folder in the Command Line, install the dependancies using pipenv install(of which are very few as my formatting in the CLI is done by hand, rather than a library) then enter the shell.  You can start the program by typing the usual 'python ' then 'lib/cli.py' if in the root folder of the program.  This will bring up the Main Menu, and in every menu, one can quit by typing 'q' and hitting enter, and in most cases return to the Main Menu with 'm'. From the Main Menu, one can choose to either work with the Artists, which I will explain in the next paragraph, or with the Genres or Categories of music. 

# Show Albums by Genre ('s')
### Note: 'a' and 'g' are used by other commands to show just Albums or Genres for myself and not in an OOP fashion
Here you can pick a genre by typing the corresponding number to view the albums that are of that Genre.  In the sub-menu, one can add albums in that genre (you will Not be prompted to add the genre) as well as delete albums from that genre by typing the number corresponding with the album as well as 'd' then enter.  It will confirm your choice as it will then delete the album.  

# Display all Artists ('d')
There one can view all Artists in the database, with formatting in the command line tweaked a little to make things more easily readable, but not with any external library.  There, a user can also add new albums that have been recently aquired by selecting the corresponding Artist from the list.  Then, in that sub-menu one can add a new album by that artist without needing to type the Artist's name again.  If one selects a specific album, the next sub-menu has options to update or delete that album, and since one is only viewing a single album, no identifying information is needed.  
