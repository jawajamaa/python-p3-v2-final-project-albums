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
    blues = Genre.create(name = "Blues")
    drum_n_bass = Genre.create(name = "Drum'n'Bass")
    house = Genre.create(name = "House")
    jazz = Genre.create(name = "Jazz")
    metal = Genre.create(name = "Metal")
    nu_metal = Genre.create(name = "Nu-Metal")
    psychedelic_soul = Genre.create(name = "Psychedelic Soul")
    punk = Genre.create(name = "Punk")
    rock = Genre.create(name = "Rock")
    soul_jazz = Genre.create(name = "Soul-Jazz")
    techno = Genre.create(name = "Techno")


    Album.create("Live", "Gary Clark, Jr.", 2014, blues)
    Album.create("New Forms", "Roni Size/Reprazent", 1998, drum_n_bass)
    Album.create("Funk the System", "DJ Dan", 1999, house)
    Album.create("Cannonball in Japan", "Cannonball Adderley", 1966, jazz)
    Album.create("I Put a Spell on You", "Nina Simone", 1965, jazz)
    Album.create("Pastel Blues", "Nina Simone", 1965, jazz)
    Album.create("Lateralus", "Tool", 2002, nu_metal)
    Album.create("Master of Puppets", "Metallica", 1987, metal)
    Album.create("The Sound of Ultimate Bass", "Carl Cox", 1998, techno)
    Album.create("Aerosmith", "Aerosmith", 1973, rock)
    Album.create("Blind Melon", "Blind Melon", 1992, rock)
    Album.create("High Voltage", "AC/DC", 1976, rock)
    Album.create("Dirty Deeds Done Dirt Cheap", "AC/DC", 1976, rock)
    Album.create("Back in Black", "AC/DC", 1980, rock)
    Album.create("Cold as Weiss", "Delvon Lamarr Organ Trio", 2022, soul_jazz)
    Album.create("Close but No Cigar", "Delvon Lamarr Organ Trio", 2018, soul_jazz)
    Album.create("Chronicles of a Diamond", "Black Pumas", 2023, psychedelic_soul)
    Album.create("Ixnay on the Hombre", "The Offspring", 1997, punk)
    Album.create("My Sound (1993 - 2004)", "Dillinja", 2004, drum_n_bass)


seed_database()
print("Database seeded, now it's up to you!")

    
