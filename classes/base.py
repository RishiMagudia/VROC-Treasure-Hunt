import pygame

class Base(object):

    def __init__(self, name = None, size = None, pos = None, stat = None, col = None, img = None):
        """
            initialise the class with optional values, can be added later
            Core/Base class for the objects that are used in the projects
        """
        self.name = name
        self.size = size
        self.position = pos
        self.colour = col
        self.image = img
        self.state = stat
        
    #getters and setters / handlers
    #setters might need changing for PyGame implementation

    #name of object
    def getName(self):
        return self.name
    def setName(self, name):
        if type(name) is str:
            self.name = name
        else:
            raise ValueError

    #state of object
    def getState(self):
        return self.state
    def setState(self, string):
        if type(string) is str:
            self.state = string
        else:
            raise ValueError

    #size of object
    def getSize(self):
        self.size
    def setSize(self, size):
        #auto converts to grid system
        self.size = size*40
        self.image = pygame.transform.scale(self.image, (size*40, size*40))

    #image of object
    def getImage(self):
        return self.image
    def setImage(self, image):
        self.image = pygame.image.load(image)

    #position of object
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        try:
            if len(position) == 2 and type(position) is tuple:
                self.position = (position[0]*40,position[1]*40)
        except:
            raise ValueError

    #colour of object
    def getColour(self):
        return self.colour
    def setColour(self, colour):
        try:
            if len(colour) == 3 and type(colour) is tuple:
                self.colour = colour
        except:
            raise ValueError
