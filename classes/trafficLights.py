import pygame
import sys
from pygame.locals import*

pygame.init()
class trafficLights:
    def trafficLights():
        win = GraphicWin()
        red = Circle(Point(100, 50), 20)
        red.setFill("black")
        red.draw(win)
        amber = Circle(Point(100,100), 20)
        amber.setFill("black")
        amber.draw(win)
        green = Circle(Point(100, 150),20)
        green.setFill("black")
        green.draw(win)
        while True:
            import time
            time.sleep(10)
    
