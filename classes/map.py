import pygame
from pygame import *

class Map():

    def __init__(self):
        # making the list for the names of the images
        # img_name 0 is sea.png
        # img_name 1 is landmark.png
        # img_name 2 is robot.png
        # img_name 3 is traffic.png
        self.img_name = [1, "sea.png", 5, "landmark.png", 3, "robot.png", 2, "traffic.png"]
        self.priority(self.img_name)
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
    def priority(self, img_name):
        self.img_name = img_name
        for i in range(len(img_name)/2-1,0,-1):
            for m in range(0,i,2):
                if img_name[m] > img_name[m+2]:
                    temp_name = img_name[m]
                    temp_value = img_name[m+1]
                    img_name[m] = img_name[m+2]
                    img_name[m+1] = img_name[m+3]
                    img_name[m+2] = temp_value
                    img_name[m+3] = temp_name
        print img_name

Map()
