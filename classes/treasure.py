import pygame
from pygame.locals import *

class Treasure():
    def __init__(self,name = None, pos = None, size = None,ImageHolder = None, pixMove = None, colour = None, movement = None, found= False):  
        Base.__init__(self, name, pos, size)
        self.ImageHolder = ImageHolder
        self.found= found
        

    def isFound(self):                            #This returns values to the landmark class             
        if self.found== True:                     #to show the tresaure has been found and searched
            return treasure_found_serchead        
        else:
            return not_searched

    def Images(self):
        setDisplay.fill(white)

        img = pygame.image.load('Rare_Treasure_Chest.png')
        FPS = 30
        imgx = 400
        imgy = 200
        pixMove = 5
        movement = 'down'
        img1 = pygame.image.load('Gu1.png')
        img1x = 800
        img1y = 300

    def ShowingMessage(self):
        setDisplay.fill(white)

        img = pygame.image.load('treasure chest.png')
        FPS = 30
        imgx = 400
        imgy = 200
        pixMove = 5
        movement = 'down'
        img1 = pygame.image.load('Gu1.png')
        img1x = 800
        img1y = 300
    #     while True:
    #         setDisplay.fill (white)
    #         if movement == 'down':
    #             imgy += pixMove
    #             img1x -= pixMove
    #
    #         setDisplay.blit(img, (imgx, imgy))
    #
    #         font = pygame.font.Font(None, 60)
    #         text = font.render("You have found tresuare WELL DONE", 1, (20, 10, 20))
    #         textpos = text.get_rect(centerx=setDisplay.get_width()/2)
    #         setDisplay.blit(text, textpos)
    #
    #
    #
    #         for event in pygame.event.get():
    #             print event
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    # pygame.display.update()
    # fpsTime.tick(FPS)
