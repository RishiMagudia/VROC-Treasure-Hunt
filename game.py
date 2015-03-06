import pygame, time

#import team's objects
import classes as c


ENABLE_GRID = False

class Game:
    """
        Main class to start the game.
    """
    #temp col, wall holder    
    def __init__(self, width=1280, height=720, wallpaper="images/background.jpg", colour=(255, 255, 255)):
        """
            initialise the game
        """
        pygame.init()

        #set the frames
        global FPS
        FPS = 60

        #contain world items
        self.land = []
        self.walls = []
        self.listOfLandmarks = []
        self.landmarkCounter = 0
        self.treasures = []
        self.visited = []
        self.loadup = []
        self.callMsgStatus = False
        
        #set the resolution of the window
        self.width = width
        self.height = height

        self.colour = colour

        #set up the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
       
        self.icon=pygame.image.load("images/pirate1.png")
        self.icon= pygame.transform.scale(self.icon,(32,32))
        pygame.display.set_icon(self.icon)
        
       
                            
        self.title = pygame.display.set_caption("Virtual Robot Obstacle Course")
        
        #set background colour/image
        #self.background = pygame.Surface(self.screen.get_size())
        #self.background = self.background.convert()
        #self.background.fill(colour)

        #load up image, resize it and blit it to the background
        self.wallpaper = pygame.image.load(wallpaper)
        self.wallpaper = pygame.transform.scale(self.wallpaper, self.screen.get_size())

        #assign the classes
        self.map = c.Map()
        self.inventory = c.Inventory()
        self.pirate = c.robot()
        self.treasure = c.Treasure()
        self.landmark = c.Landmark()
        self.trafficLight = c.trafficLights()
        self.AStar = c.AStar()
        self.interface = c.Interface(self.screen)

        #set up each of the classes with default attributes
        #?pass them on to the setup function
        #proceed to the loop

        #set up font for game
        self.font = pygame.font.SysFont("monospace", 24)
        #set up the score board
        self.TIMER = False

    def setup(self):
        """
            set up the game using team methods
            generate map, place items, randomise variables
            draw ui
        """

    def playIntro(self):
        """
            play intro animation at start
            !needs enhancement
        """
        img = pygame.image.load("images/pirate.png")
        text = pygame.image.load("images/text.png")
        wall = pygame.image.load("images/wall.jpg")
        wall = pygame.transform.scale(wall, (self.width, self.height))
        x = 600
        y = 600
        s = 5

        while True:
            y -= s
            #get pygame events
            self.screen.blit(wall, (0,0))
            for event in pygame.event.get():
                #stop running if the window is closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                #stop running if esc key pressed
                if event.type == pygame.KEYDOWN:
                    return False
            if y == 100:
                pygame.time.delay(3000)
                break
            #update the screen and images
            self.screen.blit(text, (0,0))
            self.screen.blit(img, (x,y))
            pygame.display.update()
            pygame.time.Clock().tick(FPS)

    def loop(self):
        """
            infinite loop to keep the images updating and moving
        """
        st = time.time()
        paused = False
        typing = False
        word = None
        curr_tab = None
        objects = []
        selected_item = None

        NAME = None
        TYPE = None
        IMAGE = None
        POSITION = None

        STORED = False

        while 1:
            pos = pygame.mouse.get_pos()
            #loop for the pausing of the game
            while paused == True:
                self.pause = self.font.render("PAUSED", 1, self.colour)
                self.screen.blit(self.pause, (self.width-100, 0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            paused = False

            while typing == True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            NAME = word
                            typing = False
                            break
                        else:
                            # combine letters into a word
                            if event.key == pygame.K_BACKSPACE:
                                word = word[:-1]

                                if curr_tab is self.interface.TREASURES:
                                    self.interface.open_treasures()
                                if curr_tab is self.interface.TRAPS:
                                    self.interface.open_traps()
                                if curr_tab is self.interface.LANDMARKS:
                                    self.interface.open_landmarks()
                                if curr_tab is self.interface.ROBOTS:
                                    self.interface.open_robot()

                            if len(word) < 10 and event.key != pygame.K_BACKSPACE:
                                word += chr(event.key)

                                if curr_tab is self.interface.TREASURES:
                                    self.interface.open_treasures()
                                if curr_tab is self.interface.TRAPS:
                                    self.interface.open_traps()
                                if curr_tab is self.interface.LANDMARKS:
                                    self.interface.open_landmarks()
                                if curr_tab is self.interface.ROBOTS:
                                    self.interface.open_robot()
                            else:
                                break

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                if typing == True:
                    t = self.font.render(word, 1, (0,0,0))
                    self.screen.blit(t, self.interface.TEXT_POS)
                    pygame.display.flip()
                    self.interface.draw()
                else:
                    break
            self.screen.blit(self.wallpaper, (0,0))
            self.interface.draw()
            #get pygame events and do something
            for event in pygame.event.get():

                #stop running if the window is closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                #key preses
                if event.type == pygame.KEYDOWN:
                    #escape button checker for exiting
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        break
                    print chr(event.key)
                    #P button checked for pausing
                    if event.key == pygame.K_p and typing is False:
                            paused = True
                    #get cursor click
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        print pos
                        if self.interface.drawable_area(pos) and (NAME and TYPE and IMAGE and POSITION) is not None:
                            self.interface.library.insert(NAME, TYPE, IMAGE, POSITION)
                            STORED = True
                            selected_item = None
                            curr_tab = None
                            self.interface.open_imager = []
                            self.interface.landmarks()
                            self.interface.traps()
                            self.interface.treasures()
                            self.interface.robots()
                            pygame.display.flip()
                    #placing landmarks
                    #checking if buttons are pressed

                    if self.interface.OPEN:
                        for i in self.interface.placeables:
                            if self.interface.placeables[i].collidepoint(pos):
                                try:
                                    selected_item = self.interface.open_imager[i-20]
                                    if TYPE == self.interface.TREASURES:
                                        IMAGE = self.interface.tr_images[i-20]
                                    if TYPE == self.interface.LANDMARKS:
                                        IMAGE = self.interface.lm_images[i-20]
                                except:
                                    selected_item = self.interface.open_imager[i-30]
                                    if TYPE == self.interface.TREASURES:
                                        IMAGE = self.interface.tr_images[i-30]
                                    if TYPE == self.interface.LANDMARKS:
                                        IMAGE = self.interface.lm_images[i-30]

                    for i in self.interface.clickables:
                        if self.interface.clickables[i].collidepoint(pos):
                            print self.interface.clickables[i], i
                            if i is not self.interface.TEXT and i is not self.interface.START \
                                    and i is not self.interface.STOP and i is not self.interface.RESET:
                                curr_tab = i
                                TYPE = i
                            if self.interface.OPEN:
                                self.interface.open_imager = []
                                self.interface.landmarks()
                                self.interface.traps()
                                self.interface.treasures()
                                self.interface.robots()
                                pygame.display.flip()
                            if i is self.interface.TREASURES:
                                self.interface.open_treasures()
                            if i is self.interface.TRAPS:
                                self.interface.open_traps()
                            if i is self.interface.LANDMARKS:
                                self.interface.open_landmarks()
                            if i is self.interface.ROBOTS:
                                self.interface.open_robot()

                            if i is self.interface.TEXT:
                                print self.interface.clickables[i], i, "text"
                                # reset word and set to typing
                                word = ""
                                typing = True

                            if i is self.interface.START:
                                self.TIMER = 1
                            if i is self.interface.STOP:
                                self.TIMER = 0
                            if i is self.interface.RESET:
                                self.TIMER = 2

            #update the screen and images
            #self.screen.blit(self.wallpaper, (0,0))

            if ENABLE_GRID == True:
                for x in range(0,32):
                    for y in range(0,18):
                        pygame.draw.rect(self.screen,(0,0,0),(40*x,40*y,40,40),3)

                #highlighting a specific square
                xcood = 0
                ycood = 0
                pygame.draw.rect(self.screen,(0,255,0),(40*xcood,40*ycood,40,40),3)

            if selected_item != None and word != None:
                self.screen.blit(selected_item[0], pos)
                POSITION = "%s %s" % (pos[0], pos[1])

            if self.interface.OPEN:
                for i in self.interface.open_imager:
                    if curr_tab is self.interface.TREASURES:
                        self.screen.blit(i[0], i[1])
                    if curr_tab is self.interface.TRAPS:
                        self.screen.blit(i[0], i[1])
                    if curr_tab is self.interface.LANDMARKS:
                        self.screen.blit(i[0], i[1])
                    if curr_tab is self.interface.ROBOTS:
                        self.screen.blit(i[0], i[1])

            if STORED == True:
                for n,t,i,p  in self.interface.library.display():
                    p = str(p).split(" ")
                    img = pygame.image.load(str(i))
                    img = pygame.transform.scale(img, (200, 200))
                    self.screen.blit(img, (int(p[0]), int(p[1])))

            f = pygame.font.SysFont("monospace", 42)
            t = f.render("00:00", 1, (255,255,255))
            self.screen.blit(t, (self.width-140, self.height-60))

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    window = Game()
    window.playIntro()
    window.setup()
    window.loop()
