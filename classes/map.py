import pygame
from pygame import *

class Map():

    def __init__(self):
        # making the list for the names of the images
        # img_name 0 is sea.png
        # img_name 1 is landmark.png
        # img_name 2 is robot.png
        # img_name 3 is traffic.png
        self.img_name = ["sea.png", "landmark.png", "robot.png", "traffic.png"]
        self.images()
    def image(self, img_num):
        # taking the requested img_name and looping though all the names
        # until correct name is found and load the image with that name from
        # images folder
        self.img_num = img_num
        for i in range(len(self.variables)):
            if i == self.img_num:
                pygame.image.load(images.self.variables[i])
    def drawMap():
        pygame.image.load(images.treasure_chest)
    def drawObstacle():
        print "test"
    def drawRobot():
        print "test"
    def drawTreasure():
        print "test"
    def drawButton():
        print "test"
Map()
