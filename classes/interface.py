import pygame

class Interface:

    def __init__(self, screen):

        self.__screen = screen
        self.__width, self.__height = self.__screen.get_size()

        self.drawables = {}
        self.clickables = {}
        self.imager = []
        self.tab_img = {}

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
        self.robots()
        self.timer()

        self.OPEN = False

        # CONSTANTS
        self.LANDMARKS = 6
        self.TREASURES = 7
        self.TRAPS = 8
        self.ROBOTS = 9

        self.START = 3
        self.RESET = 4
        self.STOP = 5

        # self.open_landmarks()
        # self.open_treasures()
        # self.open_traps()

        self.sprites = []

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
        for i in self.tab_img:
            c, s = self.tab_img[i]
            pygame.draw.rect(self.__screen, c, s)

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
        
        if self.OPEN == False:
            self.tab_img = {}

    def open_landmarks(self):
        """
        Landmarks holder.
        :return:
        """
        width = 185
        height = 250
        block_width = 50
        block_height = 50
        x = width*2+42
        y = self.__height-self.btn_heights-height+100
        double = 0
        c = 20

        landmarks = (100,130,130), (width*2+35, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[6] = landmarks
        self.OPEN = True
        if self.OPEN == True:
            for i in treasure_list:
                if double != 3:
                    double += 1
                    bot_panel_btn = (i), (x, y, block_width, block_height)
                    x += 60
                    self.tab_img[c] = bot_panel_btn
                    c += 1
                if double == 3 and treasure_list[-1] != i:
                    y += 60
                    x = width*2+42
                    double = 0
                    bot_panel_btn = (i), (x, y, block_width, block_height)
                    self.tab_img[c] = bot_panel_btn


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
        
        if self.OPEN == False:
            self.tab_img = {}

    def open_treasures(self):
        """
        Treasures holder.
        :return:
        """
        width = 185
        height = 250
        block_width = 50
        block_height = 50
        x = width*3+52
        y = self.__height-self.btn_heights-height+100
        double = 0
        c = 30

        treasures = (100,130,130), (width*3+45, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[7] = treasures
        self.OPEN = True

        if self.OPEN == True:
            for i in treasure_list:
                if double != 3:
                    double += 1
                    bot_panel_btn = (i), (x, y, block_width, block_height)
                    x += 60
                    self.tab_img[c] = bot_panel_btn
                    c += 1
                if double == 3 and treasure_list[-1] != i:
                    y += 60
                    x = width*3+52
                    double = 0
                    bot_panel_btn = (i), (x, y, block_width, block_height)
                    self.tab_img[c] = bot_panel_btn

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
        
        if self.OPEN == False:
            self.tab_img = {}

    def open_traps(self):
        """
        Trap selector.
        :return:
        """
         width = 185
        height = 250
        block_width = 50
        block_height = 50
        x = width*4+62
        y = self.__height-self.btn_heights-height+100
        double = 0
        c = 40

        traps = (100,130,130), (width*4+55, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[8] = traps
        self.OPEN = True

        if self.OPEN == True:
            for i in treasure_list:
                if double != 3:
                    double += 1
                    bot_panel_btn = (i), (x, y, block_width, block_height)
                    x += 60
                    self.tab_img[c] = bot_panel_btn
                    c += 1
                if double == 3 and treasure_list[-1] != i:
                    y += 60
                    x = width*4+62
                    double = 0
                    bot_panel_btn = (i), (x, y, block_width, block_height)
                    self.tab_img[c] = bot_panel_btn

    def robots(self):
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
        self.OPEN = False

    def open_robot(self):
        """
        Robot selector.
        :return:
        """
        width = 100
        height = 250

        robots = (100,130,130), (1000, self.__height-self.btn_heights-height, width, self.__height)
        self.drawables[9] = robots
        self.OPEN = True

    def timer(self):
        """
        Timer.
        :return:
        """
        width = 130
        timer = (100,100,130), (self.__width-width-10, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[10] = timer

    def create(self, name = "Name", t = None, score = None):
        """
        Sprite holder.
        """
        self.sprites.append((name, t, score))

    def drawable_area(self, o, grid = False):
        """
        o: tuple x,y coordinates.
        Checks if the object is in the drawable area.
        """
        allowed = False
        height = range(0, self.__height-75)
        width = range(0, self.__width-150)
        if grid:
            if o[0]*40 in width and o[1]*40 in height:
                allowed = True
            else:
                allowed = False
        else:
            if o[0] in width and o[1] in height:
                allowed = True
            else:
                allowed = False

        return allowed

