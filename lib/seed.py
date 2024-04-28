#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.album import Album

def seed_database():
    Genre.drop_table()
    Album.drop_table()
    Genre.create_table()
    Album.create_table()

    # create seed data
    jazz = Genre.create(name = "Jazz")
    rock = Genre.create(name = "Rock")
    house = Genre.create(name = "House")
    trance = Genre.create(name = "Trance")
    techno = Genre.create(name = "Techno")
    metal = Genre.create(name = "Metal")
    nu_metal = Genre.create(name = "Nu-Metal")
    blues = Genre.create(name = "Blues")
    drum_n_bass = Genre.create("Drum'n'Bass")

    Album.create("Blind Melon", "Blind Melon", 1992, rock)
    Album.create("Cannonball in Japan", "Cannonball Adderley", 1966, jazz)
    Album.create("Pastel Blues", "Nina Simone", 1965, jazz)
    Album.create("Master of Puppets", "Metalica", 1987, metal)
    Album.create("The Sound of Ultimate Bass", "Carl Cox", 1998, techno)
    Album.create("Lateralus", "Tool", 2002, nu_metal)
    Album.create("Temptation", "Chistopher Lawrence", 1998, trance)
    Album.create("Live", "Gary Clark, Jr.", 2014, blues)
    Album.create("New Forms", "Roni Size/Reprazent", 1998, drum_n_bass)
    Album.create("We Are Twisted!", "Various Artists", 1999, house)

seed_database()
print("Database seeded, now it's up to you!")

    
