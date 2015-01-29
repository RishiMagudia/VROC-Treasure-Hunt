from base import Base
class Treasure(Base):
    def __init__(self,name = None, pos = None, size = None,imageHolder = None, colour = None, movement = None, found= False,):  
        Base.__init__(self, name, pos, size, colour)
        self.imageHolder = imageHolder
        self.movement = movement
        self.found= found

    def showMessage(self, text, (x, y)):
        screenText = font.render(text, True, (255,0,0))
        self.screen = gameDisp
        gameDisp.blit(screenText, (x, y))
      
