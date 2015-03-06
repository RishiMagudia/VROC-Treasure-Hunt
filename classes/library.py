import sqlite3, sys

class Library:

    def __init__(self):
        """
            Library for the objects that can be created.
        """
        self.connection = None
        self.cursor = None
        self.db = "data.sqlite"
        try:
            self.connection = sqlite3.connect(self.db)
            self.cursor = self.connection.cursor()

            self.cursor.execute('''CREATE TABLE data
                                    (name TEXT,
                                     type TEXT,
                                     image TEXT,
                                     position TEXT)
                                ''')
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            # sys.exit(1)

        finally:
            if self.connection:
                self.connection.close()

    def open(self):
        try:
            self.connection = sqlite3.connect(self.db)
            self.cursor = self.connection.cursor()
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

    def close(self):
        if self.connection:
                self.connection.close()

    def insert(self, name, t, image, position):
        self.open()
        self.cursor.execute("INSERT INTO data VALUES (?, ?, ?, ?)", (name, t, image, position))
        self.connection.commit()
        self.close()

    def update_position(self, i, u):
        self.open()
        self.cursor.execute("UPDATE data SET position='%s' WHERE name='%s'" % (u, i))
        self.connection.commit()
        self.close()

    def remove(self, i, x):
        self.open()
        self.cursor.execute("DELETE * FROM data WHERE %s='%s'" % (i, x))
        self.connection.commit()
        self.close()

    def select(self, i, x):
        self.open()
        r = self.cursor.execute("SELECT * FROM data WHERE %s='%s'" % (i ,x))
        return r.fetchall()
        self.close()

    def display(self):
        self.open()
        r = self.cursor.execute("SELECT * FROM data")
        return r.fetchall()
        self.close()