import pygame

class Interface:

    def __init__(self, screen):

        self.__screen = screen
        self.__width, self.__height = self.__screen.get_size()

        self.drawables = []
        self.clickables = []

        self.btn_heights = 65
        self.btn_padding = 10

        self.sidePanel()

        # Bottom panel and buttons.
        self.botPanel()
        self.start()
        self.reset()
        self.stop()
        self.landmarks()
        self.treasures()
        self.traps()
        self.robot()
        self.timer()


    def draw(self):
        """
        Draw the UI.
        :return:
        """
        for s, c, z in self.drawables:
            pygame.draw.rect(s,c,z)

    def sidePanel(self):
        height = self.__height
        width = 150

        side_panel = self.__screen, (175,175,175), (self.__width-width, 0, width, height)
        self.drawables.append(side_panel)

    def botPanel(self):
        height = 75
        width = self.__width

        bot_panel = self.__screen, (175,175,175), (0, self.__height-height, width, height)
        self.drawables.append(bot_panel)

    def start(self):
        """
        Start Game.
        :return:
        """
        width = 125

        start = self.__screen, (130,130,130), (0, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables.append(start)

    def  reset(self):
        """
        Reset the arena.
        :return:
        """
        width = 125

        reset = self.__screen, (100,100,100), (width, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables.append(reset)

    def stop(self):
        """
        Stop the game progress.
        :return:
        """
        width = 125

        stop = self.__screen, (130,130,130), (width*2, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables.append(stop)

    def landmarks(self):
        """
        Landmarks selector.
        :return:
        """
        width = 125*1.5

        landmarks = self.__screen, (100,130,130), (width*2.2, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables.append(landmarks)

    def treasures(self):
        """
        Treasure selector.
        :return:
        """
        width = 125*1.5

        treasures = self.__screen, (100,130,130), (width*3.2, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables.append(treasures)

    def traps(self):
        """
        Trap selector.
        :return:
        """
        width = 125*1.5

        traps = self.__screen, (100,130,130), (width*4.2+1, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables.append(traps)

    def robot(self):
        """
        Robot selector.
        :return:
        """
        width = 100

        robot = self.__screen, (100,100,130), (1000, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables.append(robot)

    def timer(self):
        """
        Timer.
        :return:
        """
        width = 130

        robot = self.__screen, (100,100,130), (self.__width-width-10, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables.append(robot)