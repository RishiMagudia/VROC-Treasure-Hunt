import pygame
from pygame import *
class Base:
    def __init__(self):
        # just for testing if the sort function works
        pirate = ("pirate", (100,200), 4)
        background = ("sea", (0,0), 1)
        treasure = ("treasure", (200,250), 3)
        island = ("island", (150,250), 2)
        self.img_list = [pirate, background, treasure, island]
class Map:
    
    def __init__(self):
        # starting off the class
        self.base = Base()
        self.priority2()
    def drawMap(self):
        #drawing the map
        running = True
        while running == True:
            for i in self.base.sList:
                name, coordiantes, priority = i
                for i in range(len(self.base.img_list),0,1):
                    screen.blit(name,(coordinates))
    def priority(self):
        # using bubble sorting to priotitize image printing order
        pList = []
        # unpackage all packages and store priority in a list
        for n in self.base.img_list:
            pList.append(n[2])
        # sort out the packages by priority using bubble sort
        for i in range(len(pList)-1,0,-1):
            for m in range(0,i,1):
                if pList[m] > pList[m+1]:
                    holder = self.base.img_list[m+1]
                    self.base.img_list[m+1] = self.base.img_list[m]
                    self.base.img_list[m] = holder
                    pholder = pList[m+1]
                    pList[m+1] = pList[m]
                    pList[m] = pholder
        #self.drawMap()
    def priority2(self):
        # using a different method for sorting
        pList = []
        # unpackage all packages and store priority in a list
        for n in self.base.img_list:
            pList.append(n[2])
        # sort the created list
        pList = sorted(pList)
        # create a new list to store the package into but in a sorted manner
        sList = []
        # compare the priority to the unsorted list and if prioritys mach
        # add the package into the new sorted list
        for i in range(len(pList)):
            for m in self.base.img_list:
                if m[2] == pList[i] and m not in sList:
                    sList.append(m)
        print sList
        #self.drawMap()


Map()
