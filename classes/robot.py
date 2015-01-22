from base import Base

class robot(Base):

    def __init__(self,endPos):
        Base.__init__(self,name=None,size=None,pos=None,stat=None,col=None,img=None)
        self.velocity = 10
        self.hasReachedDestination = False
        self.endPosition = endPos

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



