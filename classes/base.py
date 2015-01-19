class Base(object):

    #keep a list of objects
    global items
    items = []
    
    def __init__(self, name, size, pos, stat, col = None, img = None):
        self.name = name
        self.size = size
        self.position = pos
        self.colour = col
        self.image = img
        self.state = stat

        #create id for object for retrieval
        self.id = 0
        #add it to a retrievable list
        items.append(self.id)
        
    #getters and setters / handlers
    #setters might need changing for PyGame implementation

    #state of object
    def getState(self):
        return self.state
    def setState(self, string):
        self.state = string

    #size of object
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size

    #image of object
    def getImage(self):
        return self.image
    def setImage(self, image):
        self.image = image

    #position of object
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position

    #colour of object
    def getColour(self):
        return self.colour
    def setColour(self, colour):
        self.colour = colour

    #return ID of object
    def getId(self):
        return self.id

    #display list of items
    def getItems(self):
        return self.items
    #clear the list of items
    def clearItems(self):
         items = []
    #delete a specific object
    def delItem(self, ID):
        if ID in self.items:
            items.remove(ID)
