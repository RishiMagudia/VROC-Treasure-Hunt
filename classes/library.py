from landmark import Landmark
from treasure import Treasure
from trafficLights import trafficLights
from robot import robot

#------------------------------------------------------------------
#? replace with sql / +save & load features
#! enhancement can be made with sql
#------------------------------------------------------------------

class Library:

    #! Global Constants -------------------------------------------
    global KEY, NAME, TYPE, SIZE, IMAGE, POSITION

    KEY = 0
    NAME = 1
    TYPE = 2
    SIZE = 3
    IMAGE = 4
    POSITION = 5
    # -------------------------------------------------------------
    def __init__(self):
        """
            Library for the objects that can be created.
        """
        self.lib = []               #list of objects

    # Library Handlers --------------------------------------------

    def create(self, name, t, size, image, (x, y)):
        """
            Create object with key.
        """
        key = len(self.lib)+1       #unique identifier
        self.lib.append([key, name, t, size, image, (x, y)])

    def selectByKey(self, key):
        """
            Select the object by key.
        """
        for i in self.lib:
            if key == i[KEY]:
                return i

    def selectByType(self, t):
        for i in self.lib:
            if t == i[TYPE]:
                return i

    def remove(self, key):
        """
            Remove the object by key.
        """
        self.lib.remove(self.selectByKey(key))

    def display(self):
        """
            Return the list of objects.
        """
        return self.lib
    # -------------------------------------------------------------

    # Getters/Setters for the object list. ------------------------

    def getName(self, key):
        return self.selectByKey(key)[NAME]

    def setName(self, key, n):
        self.selectByKey(key)[NAME] = n

    def getType(self, key):
        return self.selectByKey(key)[TYPE]

    def setType(self, key, t):
        self.selectByKey(key)[TYPE] = t

    def getSize(self, key):
        return self.selectByKey(key)[SIZE]

    def setSize(self, key, s):
        self.selectByKey(key)[SIZE] = s

    def getImage(self, key):
        return self.selectByKey(key)[IMAGE]

    def setImage(self, key, i):
        self.selectByKey(key)[IMAGE] = i

    def getPosition(self, key):
        return self.selectByKey(key)[POSITION]

    def setPosition(self, key, (x, y)):
        self.selectByKey(key)[POSITION] = (x, y)
    # -------------------------------------------------------------