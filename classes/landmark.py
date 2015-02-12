from base import Base
import pygame #This is an example of using an API to import the external library pygame.

# Initialize attributes for Landmark.

class Landmark(Base):
    
    def __init__(self, name = None, size = None, pos = None, img = None, stat = None, desc = None):# Atributes of Landmark are Initialized.
        Base.__init__(self, name, size, pos, img, stat) #Initialize inherited attributes, from Base. This is an example of inheritance.
        self.searched = False
        self.decription = 'desc'
        self.SearchedLandmarkList = []
        self.UnsearchedLandmarkList = []
        self.validLandmarksList = []

    def getSearched(self):
        return self.searched

    def setSearched(self,i):
        self.searched = i
            
    def searched(self, robotVisited): #Method checks if robot position matches any treasure position. Matches can be assumed to be searched landmarks and are made into a list, which is then returned. This is kept public so it can be called elsewhere.

        for treasure in landmarkList:  #Checks if each value in landmarkList is equal to any past or present robot position, if yes they are appended to a list.
            if treasure in robotVisited:
                 self.searchedLandmarkList.append(treasure) 

        return self.searchedLandmarkList #This list is returned  

    def __unsearched(self, landmarkList): #Method checking if each landmark has been searched. If they haven't, they are appended to a list. This calls on the Searched method. Also, this method is private, so that it is not called outside of the class. This is an example of encapsulation.

        self.unsearchedLandmarkList = [] #This list is emptied each time the method is called, to insure that no Landmarks which were unsearched previously which are now searched, are returned in the UnsearchedLandmarkList.
        
        for landmarks in landmarkList:
            if landmarks not in self.searched(robotVisited):
                self.unsearchedLandmarkList.append(landmarks)

        return self.unsearchedLandmarkList
            

    def treasurePresent(self, treasureList, landmarkList, robotVisited): #Method to check if treasure is present, by cross refrencing unsearched Landmark positions with treasure position to return a list valid positions, for the robot to travel to. As this method searches through a list of values to find a match, it is an example of a search algorithm.

        self.validLandmarksList = []

        for validLandmarks in self.__unsearched(landmarkList):
            if validLandmarks in treasureList:
                self.validLandmarksList.append(validLandmarks)

        return self.validLandmarksList 
