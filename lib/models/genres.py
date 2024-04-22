# lib/models/genres.py
from models.__init__ import CONN, CURSOR 

class Genres:

    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) and not hasattr(self, name):
            self._name = name
        else:
            raise ValueError(
                "Name must be at least one character"
            )

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

    def save(self):
        """Insert a new row with the name of the current Genre instance.  Update object id attribute using the primary key value of the new row  Save the object in the local dictionary using the PK as the dictionary key"""
        sql = """
            INSERT INTO genres (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """Initialize a new Genre instance and save the object to the database"""
        genre = cls(name)
        genre.save()
        return genre
    
    def update(self):
        """Update the table row for the current Genre instance"""
        sql = """
            UPDATE genres
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

    def delete(self):
        """Delete the table row for the current Genre instance along with the dictionary entry and reassign the id attribute"""
        sql = """
            DELETE FROM genres
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Genre object with the attribute values from the table row"""
        genre = cls.all.get(row[0])
        if genre:
            genre.name = row[1]
        else:
            genre = cls(row[1])
            genre.id = row[0]
            cls.all[genre.id] = genre
        return genre
    
