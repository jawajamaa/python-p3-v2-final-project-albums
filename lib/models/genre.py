# lib/models/genre.py
from models.__init__ import CONN, CURSOR 

class Genre:

    def __init__(self, name, id=None):
        self._id = id
        self.name = name
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # print("Genre line 23 year setter")
        if isinstance(self, Genre) and type(name) is str and len(name) >= 1:
            self._name = name

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the genres of music"""
        sql = """
            CREATE TABLE IF NOT EXISTS genres(
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Genre instances"""
        sql = """
            DROP TABLE IF EXISTS genres;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def insert(self):
        """Insert a new row with the name of the current Genre instance.  Update object id attribute using the primary key value of the new row  Save the object in the local dictionary using the PK as the dictionary key"""
        
        sql = """
            INSERT INTO genres (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,)) 
        CONN.commit()
        return Genre(self.name, CURSOR.lastrowid)

    @classmethod
    def create(cls, name):
        """Initialize a new Genre instance and save the object to the database"""
        genre = cls(name)
        return genre.insert()
    
    def update(self):
        """Update the table row for the current Genre instance"""
        sql = """
            UPDATE genres
            SET name = ?
            WHERE id is ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row for the current Genre instance along with the dictionary entry and reassign the id attribute"""
        sql = """
            DELETE FROM genres
            WHERE id is ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()


    @classmethod
    def instance_from_db(cls, row):
        """Return a Genre object with the attribute values from the table row"""
        return cls(row[1], row[0])
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Genres object per row in the table"""
        sql = """
            SELECT id, name
            FROM genres
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Genres object corresponding to the table row using the id/primary key"""
        sql = """
            SELECT id, name
            FROM genres
            WHERE id is ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Genres object corresponding to the table row using the genre name"""
        sql = """
            SELECT id, name
            FROM genres
            WHERE LOWER(name) is ?
        """
        row = CURSOR.execute(sql, (name.lower(),)).fetchone()
        return cls.instance_from_db(row) if row else None
