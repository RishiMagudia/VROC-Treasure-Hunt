import pygame
import sys
from pygame.locals import *

pygame.init()
setDisplay = pygame.display.set_mode((1200, 720))
pygame.display.set_caption('Treasure')

white = (255,0,0)
yellow = (255,255,0)


fpsTime = pygame.time.Clock()

setDisplay.fill(white)
FPS=60

class Treasure():
    def __init__(self,name, position, size,ImageHolder,ID, pixMove, FPS, colour, movement, found= True):            #Properties of my class
        self.name = name
        self.position= position
        self.size = size
        self.ImageHolder = ImageHolder
        self.ID=ID
        self.found= found
        self.pixMove = pixMove
        self.FPS = FPS
        self.colour = colour
        self.movement = movement


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
        while True:
            setDisplay.fill (white)
            if movement == 'down':
                imgy += pixMove 
                img1x -= pixMove
    
            setDisplay.blit(img, (imgx, imgy))
            
            font = pygame.font.Font(None, 60)
            text = font.render("You have found tresuare WELL DONE", 1, (20, 10, 20))
            textpos = text.get_rect(centerx=setDisplay.get_width()/2)
            setDisplay.blit(text, textpos)



            for event in pygame.event.get():
                print event
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    pygame.display.update()
    fpsTime.tick(FPS)
        
        
        

                                         
     
test = Treasure((),(),(),(),12,True, 5, 60,(255,255,0),'down' )
print test.found
found=True
movement = 'down'

test.ShowingMessage()
