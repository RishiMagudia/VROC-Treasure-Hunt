from base import Base
class Treasure(Base):
    def __init__(self,name = None, pos = None, size = None,imageHolder = None, pixMove = None, colour = None, movement = None, found= False,):  
        Base.__init__(self, name, pos, size, colour)
        self.imageHolder = imageHolder
        self.movement = movement
        self.found= found
        
        
    """
    def __isFound(self):                                      
        if self.found== True:                     
            return treasure_found_serchead        
        else:
            return not_searched 
    """
    def ShowingMessage(self, displayText, (x, y)):
      if dispayText == True:
          screenText = font.render("Treasure Found",True,(255,0,0))
          self.screen = gameDisp
          gameDisp.blit(screenText, (x, y))
      
