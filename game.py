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
        word = ""
        objects = []

        self.landmark.setImage("images/Coin.png")
        self.landmark.setSize(3)
        self.landmark.setPosition((0,0))

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

            while typing == True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.interface.landmarks()
                            self.interface.traps()
                            self.interface.treasures()
                            self.interface.robots()
                            typing = False
                            break
                        else:
                            # combine letters into a word
                            if len(word) < 10:
                                word += chr(event.key)

                                t = self.font.render(word, 1, (0,0,0))
                                self.screen.blit(t, self.interface.TEXT_POS)
                            else:
                                break
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                pygame.display.flip()

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
                    pos = pygame.mouse.get_pos()
                    print pos
                    #placing landmarks
                    #checking if buttons are pressed

                    for i in self.interface.clickables:
                        if self.interface.clickables[i].collidepoint(pos):
                            print self.interface.clickables[i], i
                            if self.interface.OPEN:
                                self.interface.landmarks()
                                self.interface.traps()
                                self.interface.treasures()
                                self.interface.robots()
                            if i is self.interface.TREASURES:
                                self.interface.open_treasures()
                            if i is self.interface.TRAPS:
                                self.interface.open_traps()
                            if i is self.interface.LANDMARKS:
                                self.interface.open_landmarks()
                            if i is self.interface.ROBOTS:
                                self.interface.open_robot()

                            if i is self.interface.TEXT:
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

            self.screen.blit(self.landmark.getImage(), self.landmark.getPosition())

            # example of allowed locations for objects checking.
            # print self.interface.drawable_area((2, 2))

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
