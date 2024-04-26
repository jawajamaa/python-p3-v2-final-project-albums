# lib/models/albums.py
from models.__init__ import CONN, CURSOR
from models.genres import Genre

class Album:

    def __init__(self, title, artist, year, genre, id=None):
        self._id = id
        self._title = title
        self._artist = artist
        self._year = year
        self._genre = genre

    def __repr__(self):
        return f"[Album id={self._id} artist=\"{self._artist}\" title=\"{self._title}\" year={self._year} genre={self._genre}]"

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title
    
    @property
    def artist(self):
        return self._artist
    
    @property
    def year(self):
        return self._year
    
    @property
    def genre(self):
        return self._genre
    
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
        """Insert a new row with the title, artist, year and genre id of the the current Album object and update the the object id using the PK from the table.  Save the object in the local dictionary using the table row's PK as dictionary key"""
        sql = """
            INSERT INTO albums (title, artist, year, genre_id)
            VALUES (?, ?, ?, ?)
        """ 
        CURSOR.execute(sql, (self._title, self._artist, self._year, self._genre.id))
        CONN.commit()

        return Album(self._title, self._artist, self._year, self._genre, CURSOR.lastrowid)
          
    @classmethod          
    def create(cls, title, artist, year, genre):
        """Initialize a new instance of Albums and save the object to the db"""
        album = cls(title, artist, year, genre)
        return album.insert()
    
    def update(self):
        """Update the table row corresponding to the current instance of Albums"""
        sql = """
            UPDATE albums
            SET title = ?, artist = ?, year = ?, genre_id = ?, 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self._title, self._artist, self._year, self._genre.id, self._id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Albums instance, delete the dictionary entry and reassign the id attribute"""
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
        """Return a list containing one Albums object per table row"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Albums object corresponding to the table row using the primary key"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
            WHERE albums.id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return Albums object corresponding to the table row using the title"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
    @classmethod
    def find_by_artist(cls, artist):    
        """Return Albums object corresponding to the table row using the artitst"""
        sql = """
            SELECT title, artist, year, genres.name, genre_id, albums.id
            FROM albums LEFT JOIN genres ON (genres.id = albums.genre_id)
            WHERE artist = ?
        """
        row = CURSOR.execute(sql, (artist,)).fetchone()
        return cls.instance_from_db(row) if row else None
