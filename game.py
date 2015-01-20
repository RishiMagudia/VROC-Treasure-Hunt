import pygame
#possible use for getting images, and exiting the interface
import os, sys

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

        #set the frame
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

        #use and import other classes to create the game
        # e.g. use of map generation and items placement

    def setup(self):
        """
            set up the game using team methods
            generate map, place items, randomise variables
        """

    def drawUI(self):
        """
            set up the UI
        """

    def playHandle(self):
        """
            handle the gameplay
        """

    def playIntro(self):
        """
            play intro animation at start
        """
        img = pygame.image.load("images/pirate.png")
        text = pygame.image.load("images/text.png")
        wall = pygame.image.load("images/wall.jpg")
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
            #update the screen
            self.screen.blit(text, (0,0))
            self.screen.blit(img, (x,y))
            pygame.display.update()
            pygame.time.Clock().tick(FPS)

    def loop(self):
        """
            infinite loop to keep the images updating and moving
        """
        while 1:
            #get pygame events
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
            #update the screen
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()

if __name__ == "__main__":
    window = Game()
    window.playIntro()
    window.loop()
