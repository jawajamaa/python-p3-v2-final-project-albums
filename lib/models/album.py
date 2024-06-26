# lib/models/album.py
from models.__init__ import CONN, CURSOR
from models.genre import Genre

class Album:

    def __init__(self, title, artist, year, genre, id=None):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre
        self._id = id

# comment out after debugging as it is only used for that...
    # def __repr__(self):
    #     return f'[Album id={self._id} artist=\"{self._artist}\" title=\"{self._title}\" year=\"{self._year}\" genre={self._genre}]'

    @property
    def id(self):
        return self._id
    
    # no id setter needed...

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 1 <= len(title) <= 30:
        # if isinstance(self, Album) and type(title) is str and len(title) >= 1:
            self._title = title
        else:
            raise ValueError ("Title must be a string between 1 and 30 characters in length")
        
    @property
    def artist(self):
        return self._artist
    
    @artist.setter
    def artist(self, artist):
        if isinstance(artist, str) and 1 <= len(artist) <= 30:
        # if isinstance(self, Album) and type(artist) is str and len(artist) >= 1:
            self._artist = artist
        else:
            raise ValueError ("Artist must be a string between 1 and 30 characters in length")

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if isinstance(int(year), int) and len(str(year)) == 4:
            self._year = year
        else:
            raise ValueError ("The release year must be a 4 character integer")

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        if isinstance(self, Album) and len(genre.name) >= 3:
            self._genre = genre

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
    
    def insert(self):
        """Insert a new row with the title, artist, year and genre id of the the current Album object and update the the object id using the PK from the table."""
        sql = """
            INSERT INTO albums (title, artist, year, genre_id)
            VALUES (?, ?, ?, ?)
        """ 
        CURSOR.execute(sql, (self.title, self.artist, self.year, self.genre.id))
        CONN.commit()

        return Album(self.title, self.artist, self.year, self.genre, CURSOR.lastrowid)
          
    @classmethod          
    def create(cls, title, artist, year, genre):
        """Initialize a new instance of Albums and save the object to the db"""
        album = cls(title, artist, year, genre)
        return album.insert()
    
    def update(self):
        """Update the table row corresponding to the current instance of Albums"""
        sql = """
            UPDATE albums
            SET title = ?, artist = ?, year = ?, genre_id = ? 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.artist, self.year, self.genre.id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Albums instance and reassign the id attribute"""
        sql = """
            DELETE FROM albums
            WHERE id = ?    
        """
        CURSOR.execute(sql,(self._id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        """Return an Albums object with the attribute values from the table row"""
        album = cls(row[0], row[1], row[2], Genre(row[3], row[4]), row[5])
        return album
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Album object per table row"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Album object corresponding to the table row using the primary key"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
            WHERE albums.id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return Album object corresponding to the table row using the title"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
    @classmethod
    def find_by_artist(cls, artist):    
        """Return Album object corresponding to the table row using the artist"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
            WHERE artist = ?
        """
        rows = CURSOR.execute(sql, (artist,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_genre(cls, genre):
        """Return a list containing an Album object per table row"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
            WHERE genres.id = ?
        """

        rows = CURSOR.execute(sql, (genre.id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def all_artists(cls):
        """Return a list containing a unique artist name"""
        sql = """
            SELECT DISTINCT artist
            FROM albums;
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
