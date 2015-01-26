import base from Base
import pygame

# Initialize attributes for Landmark.

class Landmark(Base):
    
    def __init__(self, name, size, pos, img, stat, desc):
        Base.__init__(self, name, size, pos, img, stat) #Initialize inherited attributes, from Base.
        self.decs = description
        self.name = name
        self.size = size
        self.position = pos
        self.image = img
        self.state = stat
            
    def __Searched(self): #Method checks if robot position matches any treasure position. Matches can be assumed to be searched landmarks and are made into a list, which is then returned. Variable is private, as it is only to be used in the Landmark class. This is an example of encapsulation.

        SearchedLandmarkList = [] #Makes sure that list is empty.
        
        for Treasure in Treasure_list:
            if Treasure == robot.get.position:
                 SearchedLandmarkList.append(Treasure)

        return Searched_landmark_list

    def __Unsearched(self): #Method checking if each landmark has been searched. If they haven't, they are appended to a list. 

        UnsearchedLandmarksList = [] #Makes sure list is emptied. 
        
        for Landmarks in Landmarks_list:
            if Landmarks != SearchedLanmarksList:
                Unsearched_landmarks_list.append(Landmarks)
                return UnsearchedLandmark_list
            

    def TreasurePresent(self): #Method to check if treasure is present, by cross refrencing unsearched Landmark positions with treasure position to return a list valid positions, for the robot to travel to.

        return set(self.__Unsearched) & set(treasureList) 
