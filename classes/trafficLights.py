import pygame
import time 
from pygame.locals import*
from base import Base

class trafficLights(Base):

    def __init__(self):
        Base.__init__(self)
        self.green = "images/green.png"
        self.amber = "images/amber.png"
        self.red = "images/red.png"
        self.colour = self.red

    def getColour(self):
        return self.colour

    def setColour(self, col):
        self.colour = col

    def rotateColour(self):
        if self.getColour() == self.red:
            self.setColour(self.amber)
        elif self.getColour() == self.amber:
            self.setColour(self.green)
        else:
            self.setColour(self.red)