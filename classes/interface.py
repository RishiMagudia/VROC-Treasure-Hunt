import pygame

class Interface:

    def __init__(self, screen):

        self.__screen = screen
        self.__width, self.__height = self.__screen.get_size

        self.drawables = []
        self.clickables = []

    def draw(self):
        """
        Draw the UI.
        :return:
        """

    def sidePanel(self):
        height = self.__height
        width = 100

        side_panel = pygame.draw.rect(self.__screen, (0,0,0), (self.__width-width, 0, width, height))
        self.drawables.append(side_panel)

    def botPanel(self):
        height = 100
        width = self.__width

        bot_panel = pygame.draw.rect(self.__screen, (255,255,255), (0, self.__height-height, width, height))
        self.drawables.append(bot_panel)

    def start(self):
        """
        Start Game.
        :return:
        """

    def  reset(self):
        """
        Reset the arena.
        :return:
        """

        reset = pygame.draw.rect()

    def stop(self):
        """
        Stop the game progress.
        :return:
        """

    def landmarks(self):
        """
        Landmarks selector.
        :return:
        """

    def treasures(self):
        """
        Treasure selector.
        :return:
        """

    def robot(self):
        """
        Robot selector.
        :return:
        """

    def timer(self):
        """
        Timer.
        :return:
        """