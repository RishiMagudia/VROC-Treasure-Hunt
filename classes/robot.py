from base import Base
import pygame

class robot(Base):

    def __init__(self):
        Base.__init__(self,name=None,size=None,pos=None,stat=None,col=None,img=None)
        self.velocity = 20
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

    def move(self,path,x):
        if self.getPosition()[0] < path[x]*40:
            #increment x cor
            self.setNPos((self.getPosition()[0]+self.getVelocity(),path[x+1]*40))
        if self.getPosition()[0] > path[x]*40:
            #decrease x cor
            self.setNPos((self.getPosition()[0]-self.getVelocity(),path[x+1]*40))
        if self.getPosition()[1] < path[x+1]*40:
            #increment y cor
            self.setNPos((path[x]*40,self.getPosition()[1]+self.getVelocity()))
        if self.getPosition()[1] > path[x+1]*40:
            #decrease y cor
            self.setNPos((path[x]*40,self.getPosition()[1]-self.getVelocity()))




