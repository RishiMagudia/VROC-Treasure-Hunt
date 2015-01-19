import pygame
import os, sys

class Game:
    """
        Main class to start the game.
    """
    
    def __init__(self, width=1280, height=720, colour = (255, 255, 255)):
        """
            initialise the game
        """
        pygame.init()
        
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
    window.loop()
