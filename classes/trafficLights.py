import pygame
import time 
from pygame.locals import*
from base import Base

class trafficLights(Base):

    def __init__(self):
        Base.__init__(self)
        self.timer = 3.0

        self.green = (0, 255, 0)
        self.amber = (255, 191, 0)
        self.red = (255, 0, 0)

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
