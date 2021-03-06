from base import Base
import pygame, math

class robot(Base):

    def __init__(self):
        Base.__init__(self,name=None,size=None,pos=None,stat=None,col=None,img=None)
        self.velocity = 20
        self.hasReachedDestination = True
        self.endPosition = None
        self.path = []
        self.counter = 0
        self.listOfTreasures = []

    def getVelocity(self):
        return self.velocity
    def setVelocity(self,velocity):
        self.velocity = velocity

    def getCounter(self):
        return self.counter
    def setCounter(self,x):
        self.counter = x

    def getPath(self):
        return self.path
    def setPath(self,Path):
        self.path = Path

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

    def findNearestTreasure(self):
        smallestCurrentDistance = -1
        smallestElement = -1
        for x in len(self.listOfTreasures):
            xd = self.pos[0] - self.listOfTreasures[x].getPos[0]
            yd = self.pos[1] - self.listOfTreasures[x].getPos[1]
            distance = math.sqrt(xd*xd+yd*yd)
            if smallestCurrentDistance == -1:
                smallestCurrentDistance = distance
            else:
                if distance < smallestCurrentDistance:
                    smallestCurrentDistance = distance
                    smallestElement = x
        return smallestElement
                    
            
            
            



