import pygame, random, time

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

        #buttons
        self.buttons = []

    def setup(self):
        """
            set up the game using team methods
            generate map, place items, randomise variables
            draw ui
        """

    
        # sidePanelSize = 200
        # menuPanelSize = 75
        #
        # spacing = 10
        #
        # #pirate
        # self.buttons.append(pygame.draw.rect(self.screen, (0, 255, 0), \
        #                  (spacing, self.height-menuPanelSize, menuPanelSize, menuPanelSize)))
        #
        # #landmarks
        # self.buttons.append(pygame.draw.rect(self.screen, (0, 0, 255), \
        #             (menuPanelSize+spacing*2, self.height-menuPanelSize, menuPanelSize*5, menuPanelSize)))
        #
        # #treasure
        # self.buttons.append(pygame.draw.rect(self.screen, (0, 255, 255), \
        #                  (menuPanelSize*6+spacing*3, self.height-menuPanelSize, menuPanelSize*5, menuPanelSize)))
        

        print self.buttons

    # def interface(self):
    #     """
    #     Temporary holder for the interface.
    #     """
    #
    #
    #     sidePanelSize = 200
    #     menuPanelSize = 75
    #
    #     spacing = 10
    #
    #     # tl, tr
    #     # bl, br
    #
    #     # menuPanel
    #     pygame.draw.rect(self.screen, (0, 0, 0), \
    #                      (0,self.height-menuPanelSize, self.width, self.height))
    #     # sidePanel
    #     pygame.draw.rect(self.screen, (255, 0, 0), \
    #                      (self.width-sidePanelSize, 0, self.width, self.height-menuPanelSize))
    #     # pirate
    #     pygame.draw.rect(self.screen, (0, 255, 0), \
    #                      (spacing, self.height-menuPanelSize, menuPanelSize, menuPanelSize))
    #     # landmarks
    #     pygame.draw.rect(self.screen, (0, 0, 255), \
    #                 (menuPanelSize+spacing*2, self.height-menuPanelSize, menuPanelSize*5, menuPanelSize))
    #
    #     #Treasure
    #     pygame.draw.rect(self.screen, (0, 255, 255), \
    #                      (menuPanelSize*6+spacing*3, self.height-menuPanelSize, menuPanelSize*5, menuPanelSize))

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
        while 1:
            #loop for the pausing of the game
            while paused == True:
                self.pause = self.font.render("PAUSED", 1, self.colour)
                self.screen.blit(self.pause, (self.width-100, 0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            paused = False
                        
                    
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
                    #P button checked for pausing
                    if event.key == pygame.K_p:
                            paused = True
                    #get cursor click
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print pos
                    #placing landmarks
                    pygame.draw.rect(self.screen,(255,255,0),(pos[0], pos[1],100,100),1)
                    #checking if buttons are pressed
                    for x in range(0,len(self.buttons)):
                        if self.buttons[x].collidepoint(pos):
                            if x==0:
                                print 'pirate'
                            if x==1:
                                print 'landmark'
                            if x==2:
                                print 'treasure'

                    
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

            self.interface.draw()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    window = Game()
    # window.playIntro()
    window.setup()
    window.loop()
