import pygame, library

class Interface:

    def __init__(self, screen):

        self.__screen = screen
        self.__width, self.__height = self.__screen.get_size()

        self.drawables = {}
        self.clickables = {}
        self.placeables = {}
        self.wishlist = {}
        self.treasure_list = {}
        self.imager = []
        self.tab_img = {}
        self.open_imager = []

        # tres_info = {'Goblet':'a drinking glass with a foot and a stem.','Coin':'Valuable round item','Compass':'Help to find your way','Diamond egg':'The best type of egg shiny!!','Stack of coins':'More Coins Yayy!!'}

        # SQL Library
        self.library = library.Library()

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
        self.TRSRLST = 60
        self.WISHLIST = 70

        self.TEXT = 11
        self.TEXT_POS = None

        self.START = 3
        self.RESET = 4
        self.STOP = 5

        # self.open_landmarks()
        # self.open_treasures()
        # self.open_traps()

        self.lm_images = ["Big island", "Hut", "Lighthouse", "Sunken ship", "Whale", "Small island"]
        for i in range(len(self.lm_images)):
            self.lm_images[i] = "images/"+self.lm_images[i]+".png"
        self.tr_images = ["Compass", "Diamond egg", "Goblet", "Coin", "Stack of coins", "Treasure chest"]
        for i in range(len(self.tr_images)):
            self.tr_images[i] = "images/"+self.tr_images[i]+".png"

    def draw(self):
        """
        Draw the UI.
        :return:
        """
        for i in self.drawables:
            c, s = self.drawables[i]
            pygame.draw.rect(self.__screen, c, s)
            if i != 1 and i != 2 and i != 10:
                self.clickables[i] = pygame.draw.rect(self.__screen, c, s)
        for i in self.imager:
            self.__screen.blit(i[0], i[1])
        for i in self.tab_img:
            c, s = self.tab_img[i]
            pygame.draw.rect(self.__screen, c, s)
            self.placeables[i] = pygame.draw.rect(self.__screen, c, s)

    """
        Side panel and the treasure/wishlist display.
    """
    def sidePanel(self, treasure_list = []):
        trsr_padding = 0
        width = 150

        side_panel = (175,175,175), (self.__width-width, 30, width, self.__height-85)

        img = pygame.image.load(self.panel_image)
        img = pygame.transform.scale(img, (width, self.__height-85))
        img = img, (self.__width-width+20, 23)
        self.imager.append(img)

        self.drawables[1] = side_panel

        trsr_btn = (175,175,200), (self.__width-width, 0, width/2, 28)
        wishlst_btn = (175,175,200), (self.__width-width + 78, 0, width/2, 28)
        self.drawables[60] = trsr_btn
        self.drawables[70] = wishlst_btn
        font = pygame.font.SysFont('Arial', 16)
        trsr_txt = font.render("Treasure", 1, (0,0,0))
        trsr_txt = trsr_txt, (self.__width-width+10, 3)
        wishlst_txt = font.render("Wishlist", 1, (0,0,0))
        wishlst_txt = wishlst_txt, (self.__width-width + 90, 3)
        self.imager.append(trsr_txt)
        self.imager.append(wishlst_txt)

        wish_count = 61
        for i in self.wishlist:
            if wish_count == 61:
                wish_trsr = (i), (self.__width-width, 40, width, self.__height-600)
            else:
                wish_trsr = (i), (self.__width-width, trsr_padding+50, width, self.__height-610)
            trsr_padding += 120
            wish_count += 1
            self.drawables[wish_count] = wish_trsr
        
        counter = 50
        for i in self.treasure_list:
            if counter == 50:
                found_trsr = (i), (self.__width-width, 40, width, self.__height-600)
            else:
                found_trsr = (i), (self.__width-width, trsr_padding+50, width, self.__height-610)
            trsr_padding += 120
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
        img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
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
        img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
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
        img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
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
        img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (width*2+35, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.panel_font.render("LANDMARKS", 1, (255,255,255))
        t = t, ((width*2+35)+15, self.__height-self.btn_heights+13)
        self.imager.append(t)

        self.drawables[6] = landmarks
        self.OPEN = False

        try:
            del self.drawables[100]
            self.open_imager = []
        except:
            pass

        self.tab_img = {}

    def open_landmarks(self, treasure_list = [(0,30,255), (0,0,0), (0,255,255), (0,30,155), (0,100,0), (255,100,255)]):
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

        self.text_box((240,240,240), (width*2+35, self.__height-self.btn_heights-height+10, width, 50))

        index = 0
        for i in treasure_list:
            if double != 3:
                double += 1
                bot_panel_btn = (i), (x, y, block_width, block_height)
                img = pygame.image.load(self.lm_images[index])
                img = pygame.transform.scale(img, (block_width, block_height))
                self.open_imager.append((img, (x, y)))
                index += 1
                x += 60
                self.tab_img[c] = bot_panel_btn
                c += 1
            if double == 3 and treasure_list[-1] != i:
                y += 60
                x = width*2+42
                double = 0
                bot_panel_btn = (i), (x, y, block_width, block_height)
                img = pygame.image.load(self.lm_images[index])
                img = pygame.transform.scale(img, (block_width, block_height))
                self.open_imager.append((img, (x, y)))
                self.tab_img[c] = bot_panel_btn


    def treasures(self):
        """
        Treasure selector.
        :return:
        """
        width = 185

        treasures = (100,130,130), (width*3+45, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)

        img = pygame.image.load(self.btn_image)
        img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (width*3+45, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.panel_font.render("TREASURES", 1, (255,255,255))
        t = t, ((width*3+45)+17, self.__height-self.btn_heights+13)
        self.imager.append(t)

        self.drawables[7] = treasures
        self.OPEN = False

        try:
            del self.drawables[11]
            self.open_imager = []
        except:
            pass

        self.tab_img = {}

    def open_treasures(self, treasure_list = [(0,30,255), (0,0,0), (0,255,255), (0,30,155), (0,100,0), (255,100,255)]):
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

        self.text_box((240,240,240), (width*3+45, self.__height-self.btn_heights-height+10, width, 50))
        index = 0
        for i in treasure_list:
            if double != 3:
                double += 1
                bot_panel_btn = (i), (x, y, block_width, block_height)
                img = pygame.image.load(self.tr_images[index])
                img = pygame.transform.scale(img, (block_width, block_height))
                self.open_imager.append((img, (x, y)))
                index += 1
                x += 60
                self.tab_img[c] = bot_panel_btn
                c += 1
            if double == 3 and treasure_list[-1] != i:
                y += 60
                x = width*3+52
                double = 0
                bot_panel_btn = (i), (x, y, block_width, block_height)
                img = pygame.image.load(self.tr_images[index])
                img = pygame.transform.scale(img, (block_width, block_height))
                self.open_imager.append((img, (x, y)))
                self.tab_img[c] = bot_panel_btn

    def traps(self):
        """
        Trap selector.
        :return:
        """
        width = 185

        traps = (100,130,130), (width*4+55, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)

        img = pygame.image.load(self.btn_image)
        img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (width*4+55, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.panel_font.render("TRAPS", 1, (255,255,255))
        t = t, ((width*4+55)+52, self.__height-self.btn_heights+13)
        self.imager.append(t)

        self.drawables[8] = traps
        self.OPEN = False

        try:
            del self.drawables[11]
        except:
            pass

        self.tab_img = {}

    def open_traps(self, treasure_list = [(0,30,255), (0,0,0), (0,255,255), (0,30,155), (0,100,0), (255,100,255)]):
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

        self.text_box((240,240,240), (width*4+55, self.__height-self.btn_heights-height+10, width, 50))

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
        img = pygame.transform.scale(img, (width, self.btn_heights-self.btn_padding))
        img = img, (1000, self.__height-self.btn_heights)
        self.imager.append(img)

        t = self.robot_font.render("ROBOTS", 1, (255,255,255))
        t = t, (1010, self.__height-self.btn_heights+15)
        self.imager.append(t)

        self.drawables[9] = robot
        self.OPEN = False

        try:
            del self.drawables[11]
        except:
            pass

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

        self.text_box((240,240,240), (1000, self.__height-self.btn_heights-height+10, width, 50))

    def timer(self):
        """
        Timer.
        :return:
        """
        width = 130
        timer = (100,100,130), (self.__width-width-10, self.__height-self.btn_heights, width, self.btn_heights-self.btn_padding)
        self.drawables[10] = timer

    def drawable_area(self, o, grid = False):
        """
        o: tuple x,y coordinates.
        Checks if the object is in the drawable area.
        """
        allowed = False

        # range in pixels where objects are allowed
        height = range(0, self.__height-75-200)
        width = range(0, self.__width-150-200)

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

    def text_box(self, (r, g, b), (x, y, w, h)):
        """
        Text box.
        """
        text_box = (r, g, b), (x, y, w, h)
        self.drawables[11] = text_box
        self.TEXT_POS = x, y

