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

The seed.py file contains 9 genres and 10 albums for the intial creation of the tables.  Once that is created, one can navigate into the main menu, choose to either work with the genres to view as well as add or delete new genres or navigate to the album administration section.  There one can view all albums, with formatting in the command line tweaked a little to make things more easily readable, but not with any external library.  There, a user can also add new albums that have been recently aquired, update any information that may be incorrect or delete any albums that are no longer needed in the table, all without the user seeing any of the id numbers or any of the objects unneccessarily printed out.
