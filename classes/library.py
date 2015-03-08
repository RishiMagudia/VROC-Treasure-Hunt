from treasure import Treasure
from landmark import Landmark
from robot import robot

import sqlite3, sys, os

class Library:

    def __init__(self):
        """
            Library for the objects that can be created.
        """

        self.LANDMARKS = 6
        self.TREASURES = 7
        self.TRAPS = 8
        self.ROBOTS = 9

        self.connection = None
        self.cursor = None
        self.db = "data.sqlite"
        if os.path.exists(self.db):
            os.remove(self.db)
        try:
            self.connection = sqlite3.connect(self.db)
            self.cursor = self.connection.cursor()

            self.cursor.execute('''CREATE TABLE data
                                    (name TEXT,
                                     type TEXT,
                                     image TEXT,
                                     position TEXT,
                                     object TEXT)
                                ''')
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            # sys.exit(1)

        finally:
            if self.connection:
                self.connection.close()

    def open(self):
        """
        Open the connection in the db.
        """
        try:
            self.connection = sqlite3.connect(self.db)
            self.cursor = self.connection.cursor()
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

    def close(self):
        """
        Close the connection on the db.
        """
        if self.connection:
                self.connection.close()

    def insert(self, n, t, i, p):
        """
        Insert item to the db.
        """
        self.open()
        # add the real object to the database
        o = None
        if t == self.TREASURES:
            o = Treasure()
        if t == self.LANDMARKS:
            o = Landmark()
        if t == self.ROBOTS:
            o = robot()
        # insert the query into the db
        self.cursor.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?)", (n, t, i, p, str(o)))
        self.connection.commit()
        self.close()

    def update_position(self, i, u):
        """
        Update the item position in the db.
        """
        self.open()
        # update the entity in the db
        self.cursor.execute("UPDATE data SET position='%s' WHERE name='%s'" % (u, i))
        self.connection.commit()
        self.close()

    def remove(self, i, x):
        """
        Remove select item from db.
        """
        self.open()
        # remove the entity from the db
        self.cursor.execute("DELETE * FROM data WHERE %s='%s'" % (i, x))
        self.connection.commit()
        self.close()

    def select(self, i, x):
        """
        Select and return an item from db.
        """
        self.open()
        # select the entity from the db
        r = self.cursor.execute("SELECT * FROM data WHERE %s='%s'" % (i ,x))
        return r.fetchall()
        self.close()

    def display(self):
        """
        Return all objects from db.
        """
        self.open()
        # display all entities from the db
        r = self.cursor.execute("SELECT * FROM data")
        return r.fetchall()
        self.close()
