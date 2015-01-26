import pygame
#possible use for getting images, and exiting the interface
import os, sys

import classes


ENABLE_GRID = True

class Game:
    """
        Main class to start the game.
    """

    #temp col, wall holder    
    def __init__(self, width=1280, height=720, wallpaper = None, colour = (255, 255, 255)):
        """
            initialise the game
        """
        pygame.init()

        #set the frames
        global FPS
        FPS = 60
        
        #set the resolution of the window
        self.width = width
        self.height = height

        #set up the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.title = pygame.display.set_caption("Virtual Robot Obstacle Course")
        
        #set background colour/image
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(colour)

        #assign the classes
        #self.map = classes.Map()
        #self.inventory = classes.Inventory()
        self.pirate = classes.robot()
        #self.treasure = classes.Treasure()
        #self.landmark = classes.Landmark()
        self.AStar = classes.AStar()
        
        

        #set up each of the classes with default attributes
        #?pass them on to the setup function
        #proceed to the loop

    def setup(self):
        """
            set up the game using team methods
            generate map, place items, randomise variables
            draw ui
        """
        testPirate = self.pirate
        

    def playHandle(self):
        """
            handle the gameplay
        """

    def playIntro(self):
        """
            play intro animation at start
            !needs enhancement
        """
        img = pygame.image.load("images/pirate.png")
        text = pygame.image.load("images/text.png")
        wall = pygame.image.load("images/wall.jpg")
        wall = pygame.transform.scale(wall, (self.width, self.height))
        x = 600
        y = 600
        s = 5

        while True:
            y -= s
            #get pygame events
            self.screen.blit(wall, (0,0))
            for event in pygame.event.get():
                #stop running if the window is closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                #stop running if esc key pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        break
            if y == 100:
                pygame.time.delay(3000)
                break
            #update the screen and images
            self.screen.blit(text, (0,0))
            self.screen.blit(img, (x,y))
            pygame.display.update()
            pygame.time.Clock().tick(FPS)
            
    def loop(self):
        """
            infinite loop to keep the images updating and moving
        """
        while 1:
            #get pygame events and do something
            for event in pygame.event.get():
                
                #stop running if the window is closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                #stop running if esc key pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        break
                    
            #update the screen and images /temp, to be used in playHandle
            self.screen.blit(self.background, (0,0))

            pathfind = self.AStar
            pathfind.init_grid(10,10,1,1) #start cood and end cood
            pathfind.algorithm()

            if ENABLE_GRID == True:
                for x in range(0,32):
                    for y in range(0,18):
                        pygame.draw.rect(self.screen,(0,0,0),(40*x,40*y,40,40),3)

                        #highlighting a specific square
                        xcood = 0
                        ycood = 0
                        pygame.draw.rect(self.screen,(0,255,0),(40*xcood,40*ycood,40,40),3)
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    window = Game()
    #window.playIntro()
    window.setup()
    window.loop()
