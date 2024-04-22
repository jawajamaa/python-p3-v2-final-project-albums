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
            id INTEGER PRIMARY KEY,
            title TEXT,
            artist TEXT,
            year INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES
            genres(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Album instances """
        sql = """
            DROP TABLE IF EXISTS albums;
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
          
    @classmethod          
    def create(cls, title, artist, year, genre_id):
        """Initialize a new instance of Albums and save the object to the db"""
        albums = cls(title, artist, year, genre_id)
        albums.save()
        return albums
    
    def update(self):
        """Update the table row corresponding to the current instance of Albums"""
        sql = """
            UPDATE albums
            SET title = ?, artist = ?, year = ?, genre_id = ?, 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.artist, self.year, self.genre_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Albums instance, delete the dictionary entry and reassign the id attribute"""
        sql = """
            DELETE FROM albums
            WHERE id = ?    
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return an Albums object with the attribute values from the table row"""
        album = cls.all.get(row[0])
        if album:
            album.title = row[1]
            album.artist = row[2]
            album.year = row[3]
            album.genre_id = row[4]
        else:
            album = cls(row[1],row[2],row[3],row[4])
            album.id = row[0]
            cls.all[album.id] = album
        return album
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Albums object per table row"""
        sql = """
            SELECT *
            FROM albums
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Albums object corresponding to the table row using the primary key"""
        sql = """
            SELECT *
            FROM albums
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return Albums object corresponding to the table row using the title"""
        sql = """
            SELECT *
            FROM albums
            WHERE title is ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
    @classmethod
    def find_by_artist(cls, artist):    
        pass
