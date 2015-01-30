from base import Base
import pygame

class Treasure(Base):
    def __init__(self,name = None, pos = None, size = None,imageHolder = None, colour = None, movement = None, found= False):  
        Base.__init__(self, name, pos, size, colour)
        self.imageHolder = imageHolder
        self.movement = movement
        self.found= found
        self.imageTime = 10

    def showMessage(self,gameDisp, text,cood):
        if self.imageTime > 0:
            self.font = pygame.font.SysFont("monospace", 50)
            screenText = self.font.render(text, True, (255,0,0))
            self.screen = gameDisp
            gameDisp.blit(screenText,cood)
            self.imageTime-= 1
            

        if self.image < 0:
            self.font = pygame.font.SysFont("monospace", 50)
            screenText = self.font.render(text, True, (255,0,0))
            self.screen = gameDisp
            gameDisp.blit(screenText,cood)
            self.imageTime-= 1
