#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.genres import Genres
from models.albums import Albums

def seed_database():
    Genres.drop_table()
    Albums.drop_table()
    Genres.create_table()
    Albums.create_table()

    # create seed data
    jazz = Genres.create("Jazz")
    rock = Genres.create("Rock")
    house = Genres.create("House")
    trance = Genres.create("Trance")
    techno = Genres.create("Techno")
    metal = Genres.create("Metal")
    nu_metal = Genres.create("Nu-Metal")
    blues = Genres.create("Blues")
    drum_n_bass = Genres.create("Drum'n'Bass")
    Albums.create("Blind Melon", "Blind Melon", 1992, rock.id)
    Albums.create("Cannonball in Japan", "Cannonball Adderley", 1966, jazz.id)
    Albums.create("Pastel Blues", "Nina Simone", 1965, jazz.id)
    Albums.create("Master of Puppets", "Metalica", 1987, metal.id)
    Albums.create("The Sound of Ultimate Bass", "Carl Cox", 1998, techno.id)
    Albums.create("Lateralus", "Tool", 2002, nu_metal.id)
    Albums.create("Temptation", "Chistopher Lawrence", 1998, trance.id)
    Albums.create("Live", "Gary Clark, Jr.", 2014, blues.id)
    Albums.create("The Takeover Bid Round 2", "Mickey Finn", 1992, drum_n_bass.id)

seed_database()
print("Database seeded, now it's up to you!")

    
