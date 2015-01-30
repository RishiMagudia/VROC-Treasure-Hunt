import pygame

class Base(object):

    def __init__(self, name = None, size = None, pos = None, gridPos = None, stat = None, col = None, img = None):
        """
            initialise the class with optional values, can be added later
            Core/Base class for the objects that are used in the projects
        """
        self.name = name
        self.size = size
        self.position = pos
        self.gridPos = gridPos
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
        return self.size

    def setSize(self, size):
        if size == 0:
            size = 1
        self.size = size*40
        if self.image != None:
            self.image = pygame.transform.scale(self.image, (size*40, size*40))

    #image of object
    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = pygame.image.load(image)

    #position of object and grid position
    def getPosition(self):
        return self.position

    def getGridPos(self):
        return self.gridPos

    def setPosition(self, (x, y)):
        if x == 0:
            x = 1
        if y == 0:
            y = 1
        self.position = (x*40, y*40)
        self.gridPos = (x, y)

    #robot normal position
    def setNPos(self, (x, y)):
        if x == 0:
            x = 1
        if y == 0:
            y = 1
        self.NPos = (x, y)
        self.position = (x,y)
        self.gridPos = (x/40, y/40)

    def getNPos(self):
        return self.NPos

    #colour of object
    def getColour(self):
        return self.colour

    def setColour(self, (r, g, b)):
        if (r and g and b) in range(0, 255):
            self.colour = (r, g, b)
