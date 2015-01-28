from base import Base
import pygame

class robot(Base):

    def __init__(self):
        Base.__init__(self,name=None,size=None,pos=None,stat=None,col=None,img=None)
        self.velocity = 10
        self.hasReachedDestination = True
        self.endPosition = None

    def getVelocity(self):
        return self.velocity
    def setVelocity(self,velocity):
        self.velocity = velocity

    def getHasReachedDestination(self):
        return self.hasReachedDestination
    def setHasReachedDestination(self,destinationReached):
        self.hasReachedDestination = destinationReached

    def getEndPosition(self):
        return self.endPosition
    def setEndPosition(self,endPos):
        self.endPosition = endPos

    def move(self,endPoint,):
        print 'test'
        #pygame.draw.rect(screen,(0,255,0),(40*cood[0],40*cood[1],40,40),10) #replace with pirate image at later date




