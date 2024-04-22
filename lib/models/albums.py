# lib/models/albums.py
from models.__init__ import CONN, CURSOR
from models.genres import Genres

class Albums:

    all = dict()

    def __init__(self, title, artist, year, genre_id, id=None):
        self.id = id
        self.title = title
        self.artist = artist
        self.year = year
        self.genre_id = genre_id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "Title must be a minimum of one character"
            )
        
    @property
    def artist(self):
        return self._artist
    
    @artist.setter
    def artist(self, artist):
        if isinstance(artist, str) and len(artist):
            self._artist = artist
        else:
            raise ValueError(
                "Artist's name must be a minimum of one character"
            )

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if isinstance(year, int) and len(str(year)) == 4:
            self._year = year
        else:
            raise ValueError(
                "The year must be a 4 digit integer; in other words, no music from earlier than the year 1000 AD is accepted"
            )

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of new Album instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY
            title TEXT
            artist TEXT
            year INTEGER
            genre_id INTEGER
            FOREIGN KEY (genre_id) REFERNCES
            genres(id))
        """

        CURSOR.execute(sql)
        CONN.commit()

    def drop_table(cls):
        """Drop the table that persists Album instances """
        sql = """
            DROP TABLE IF EXISTS employees;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """Insert a new row with the title, artist, year and genre id of the the current Album object and update the the object id using the PK from the table.  Save the object in the local dictionary using the table row's PK as dictionary key"""
        sql = """
            INSERT INTO albums (title, artist, year, genre_id)
            VALUES (?, ?, ?, ?)
        """ 
        CURSOR.execute(sql, (self.title, self.artist, self.year, self.genre_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
          
