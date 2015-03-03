import pygame

class Interface:

    def __init__(self, screen):

        self.__screen = screen
        self.__width, self.__height = self.__screen.get_size()

        self.drawables = {}
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

        # self.open_landmarks()
        # self.open_treasures()
        # self.open_traps()

    def draw(self):
        """
        Draw the UI.
        :return:
        """
        for i in self.drawables:
            c, s = self.drawables[i]
            pygame.draw.rect(self.__screen, c, s)

    """
        Side panel and the treasure/wishlist display.
    """
    def sidePanel(self):
        height = self.__height
        width = 150

        side_panel = (175,175,175), (self.__width-width, 0, width, height-75)
        self.drawables[1] = side_panel

    """
        Bottom panel and buttons.
    """
    def botPanel(self):
        height = 75
        width = self.__width

        bot_panel = (175,175,175), (0, self.__height-height, width, height)
        self.drawables[2] = bot_panel

    def start(self):
        """
        Start Game.
        :return:
        """
        width = 125

        start = (130,130,130), (0, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[3] = start

    def reset(self):
        """
        Reset the arena.
        :return:
        """
        width = 125

        reset = (100,100,100), (width, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[4] = reset

    def stop(self):
        """
        Stop the game progress.
        :return:
        """
        width = 125

        stop = (130,130,130), (width*2, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[5] = stop

    def landmarks(self):
        """
        Landmarks selector.
        :return:
        """
        width = 125*1.5

        landmarks = (100,130,130), (width*2.2, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[6] = landmarks

    def open_landmarks(self):
        """
        Landmarks holder.
        :return:
        """
        width = 125*1.5
        height = 250

        landmarks = (100,130,130), (width*2.2, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[0] = landmarks


    def treasures(self):
        """
        Treasure selector.
        :return:
        """
        width = 125*1.5

        treasures = (100,130,130), (width*3.2, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[7] = treasures

    def open_treasures(self):
        """
        Treasures holder.
        :return:
        """
        width = 125*1.5
        height = 250

        treasures = (100,130,130), (width*3.2, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[0] = treasures

    def traps(self):
        """
        Trap selector.
        :return:
        """
        width = 125*1.5

        traps = (100,130,130), (width*4.2+1, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[8] = traps

    def open_traps(self):
        """
        Trap selector.
        :return:
        """
        width = 125*1.5
        height = 250

        traps = (100,130,130), (width*4.2+1, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[0] = traps

    def robot(self):
        """
        Robot selector.
        :return:
        """
        width = 100

        robot = (100,100,130), (1000, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[9] = robot

    def timer(self):
        """
        Timer.
        :return:
        """
        width = 130

        timer = (100,100,130), (self.__width-width-10, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[10] = timer