import pygame
import sys
import time 
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

        color = "red"
        while True:
            for light in [ red, amber, green]:
                light.setFill( color )

                time.sleep(5)

                light.setFill( "black" )
                if color == "red":
                    color = "amber"
                elif color == "amber":
                    color = "green"
                elif color == "green":
                    color = "red"

