import pygame

class Interface:

    def __init__(self, screen):

        self.__screen = screen
        self.__width, self.__height = self.__screen.get_size()

        self.drawables = {}
        self.clickables = {}
        self.imager = []

        self.btn_heights = 65
        self.btn_padding = 10

        self.btn_image = "images/phase_btn.png"
        self.panel_image = "images/panel.png"
        self.btn_font = pygame.font.SysFont("monospace", 32)
        self.panel_font = pygame.font.SysFont("monospace", 28)
        self.robot_font = pygame.font.SysFont("monospace", 24)

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

        self.OPEN = False

        # CONSTANTS
        self.LANDMARKS = 6
        self.TREASURES = 7
        self.TRAPS = 8

        self.START = 3
        self.RESET = 4
        self.STOP = 5

        # self.open_landmarks()
        # self.open_treasures()
        # self.open_traps()

        for i in self.drawables:
            if i != 1 and i != 2 and i != 10:
                c, s = self.drawables[i]
                self.clickables[i] = pygame.draw.rect(self.__screen, c, s)

    def draw(self):
        """
        Draw the UI.
        :return:
        """
        for i in self.drawables:
            c, s = self.drawables[i]
            pygame.draw.rect(self.__screen, c, s)
        for i in self.imager:
            self.__screen.blit(i[0], i[1])

    """
        Side panel and the treasure/wishlist display.
    """
    def sidePanel(self, treasure_list = []):
        treasure_list = treasure_list
        trsr_padding = 0
        width = 150

        side_panel = (175,175,175), (self.__width-width, 0, width, self.__height-75)

        img = pygame.image.load(self.panel_image)
        img = img = pygame.transform.scale(img, (width, self.__height-75))
        img = img, (self.__width-width+20, -10)
        self.imager.append(img)

        self.drawables[1] = side_panel
        counter = 50
        for i in treasure_list:
            if counter == 50:
                found_trsr = (i), (self.__width-width, 0, width, self.__height-600)
            else:
                found_trsr = (i), (self.__width-width, trsr_padding, width, self.__height-600)
            trsr_padding += 130
            counter += 1
            self.drawables[counter] = found_trsr

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

        img = pygame.image.load(self.btn_image)
        img = img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (0, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.btn_font.render("START", 1, (255,255,255))
        t = t, (14, self.__height-self.btn_heights+10)
        self.imager.append(t)

        self.drawables[3] = start

    def reset(self):
        """
        Reset the arena.
        :return:
        """
        width = 125

        reset = (100,100,100), (width, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)

        img = pygame.image.load(self.btn_image)
        img = img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (width, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.btn_font.render("RESET", 1, (255,255,255))
        t = t, (width+14, self.__height-self.btn_heights+10)
        self.imager.append(t)

        self.drawables[4] = reset

    def stop(self):
        """
        Stop the game progress.
        :return:
        """
        width = 125

        stop = (130,130,130), (width*2, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)

        img = pygame.image.load(self.btn_image)
        img = img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (width*2, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.btn_font.render("STOP", 1, (255,255,255))
        t = t, ((width*2)+25, self.__height-self.btn_heights+10)
        self.imager.append(t)

        self.drawables[5] = stop

    def landmarks(self):
        """
        Landmarks selector.
        :return:
        """
        width = 185

        landmarks = (100,130,130), (width*2+35, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)

        img = pygame.image.load(self.btn_image)
        img = img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (width*2+35, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.panel_font.render("LANDMARKS", 1, (255,255,255))
        t = t, ((width*2+35)+15, self.__height-self.btn_heights+13)
        self.imager.append(t)

        self.drawables[6] = landmarks
        self.OPEN = False

    def open_landmarks(self):
        """
        Landmarks holder.
        :return:
        """
        width = 185
        height = 250

        landmarks = (100,130,130), (width*2+35, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[6] = landmarks
        self.OPEN = True


    def treasures(self):
        """
        Treasure selector.
        :return:
        """
        width = 185

        treasures = (100,130,130), (width*3+45, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)

        img = pygame.image.load(self.btn_image)
        img = img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (width*3+45, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.panel_font.render("TREASURES", 1, (255,255,255))
        t = t, ((width*3+45)+17, self.__height-self.btn_heights+13)
        self.imager.append(t)

        self.drawables[7] = treasures
        self.OPEN = False

    def open_treasures(self):
        """
        Treasures holder.
        :return:
        """
        width = 185
        height = 250

        treasures = (100,130,130), (width*3+45, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[7] = treasures
        self.OPEN = True

    def traps(self):
        """
        Trap selector.
        :return:
        """
        width = 185

        traps = (100,130,130), (width*4+55, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)

        img = pygame.image.load(self.btn_image)
        img = img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (width*4+55, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.panel_font.render("TRAPS", 1, (255,255,255))
        t = t, ((width*4+55)+52, self.__height-self.btn_heights+13)
        self.imager.append(t)

        self.drawables[8] = traps
        self.OPEN = False

    def open_traps(self):
        """
        Trap selector.
        :return:
        """
        width = 185
        height = 250

        traps = (100,130,130), (width*4+55, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[8] = traps
        self.OPEN = True

    def robot(self):
        """
        Robot selector.
        :return:
        """
        width = 100

        robot = (100,100,130), (1000, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)

        img = pygame.image.load(self.btn_image)
        img = img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (1000, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.robot_font.render("ROBOTS", 1, (255,255,255))
        t = t, (1010, self.__height-self.btn_heights+15)
        self.imager.append(t)

        self.drawables[9] = robot

    def timer(self):
        """
        Timer.
        :return:
        """
        width = 130
        timer = (100,100,130), (self.__width-width-10, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[10] = timer
