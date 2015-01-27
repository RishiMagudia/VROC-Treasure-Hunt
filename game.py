import pygame, random

#import team's objects
import classes as c


ENABLE_GRID = False

class Game:
    """
        Main class to start the game.
    """

    #temp col, wall holder    
    def __init__(self, width=1280, height=720, wallpaper = "images/background.jpg", colour = (255, 255, 255)):
        """
            initialise the game
        """
        pygame.init()

        #set the frames
        global FPS
        FPS = 60

        #contain world items
        self.land = []
        self.loadup = []
        
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
        
        

        #set up each of the classes with default attributes
        #?pass them on to the setup function
        #proceed to the loop

        #set up font for game
        self.font = pygame.font.SysFont("monospace", 24)
        #set up the score board


    def setup(self):
        """
            set up the game using team methods
            generate map, place items, randomise variables
            draw ui
        """
        self.pathfind = c.AStar()
        self.testPirate = c.robot()

        self.testPirate.setImage("images/pirate.png")
        self.testPirate.setSize(1)
        self.testPirate.setPosition((0, 0))
        self.loadup.append((self.testPirate, 2))

        self.testLandmark = c.Landmark()
        self.testLandmark.setImage("images/Hut.png")
        self.testLandmark.setSize(3)
        self.testLandmark.setPosition((15, 0))
        self.loadup.append((self.testLandmark, 1))

        #pirate's start point
        self.pier = c.Landmark()
        self.pier.setImage("images/Pier.png")
        self.pier.setSize(7)
        self.pier.setPosition((-1, 13))
        self.loadup.append((self.pier, 2))

        self.obs = c.Landmark()
        self.obs.setImage("images/Sunken ship.png")
        self.obs.setSize(1)

        self.map.prioritize(self.loadup)

        #generating obstacles, aka the map structure
        while len(self.land) < 64:
            xRandom = random.randint(0,7)
            yRandom = random.randint(0,5)
            if (xRandom, yRandom) not in self.land:
                self.land.append((xRandom, yRandom))

            xRandom = random.randint(7,15)
            yRandom = random.randint(5,9)
            if (xRandom, yRandom) not in self.land:
                self.land.append((xRandom, yRandom))
                
            xRandom = random.randint(15,23)
            yRandom = random.randint(9,13)
            if (xRandom, yRandom) not in self.land:
                self.land.append((xRandom, yRandom))

            xRandom = random.randint(23,31)
            yRandom = random.randint(13,17)
            if (xRandom, yRandom) not in self.land:
                self.land.append((xRandom, yRandom))



    def playHandle(self):
        """
            handle the gameplay
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
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        break
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
        while 1:
            #get pygame events and do something
            for event in pygame.event.get():
                
                #stop running if the window is closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                #stop running if esc key pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        break
                    
            #update the screen and images
            #self.screen.blit(self.background, (0,0))
            self.screen.blit(self.wallpaper, (0,0))

            if ENABLE_GRID == True:
                for x in range(0,32):
                    for y in range(0,18):
                        pygame.draw.rect(self.screen,(0,0,0),(40*x,40*y,40,40),3)

                #highlighting a specific square
                xcood = 0
                ycood = 0
                pygame.draw.rect(self.screen,(0,255,0),(40*xcood,40*ycood,40,40),3)

            #draw the inaccessible lands
            for xL, yL in self.land:
                self.screen.blit(self.obs.getImage(), (40*xL,40*yL))

            if self.testPirate.getHasReachedDestination() == True:
                self.testPirate.setHasReachedDestination(False)
                #apply next treasure to pathfind to
                treasureX = 17
                treasureY = 2
                self.pathfind.init_grid(treasureX,treasureY,2,15,self.land) #start cood and end cood + walls
                self.pathfind.algorithm()
                path = self.pathfind.getPath()
                x=0
            else:
                #traverse the path until destination is reached
                try:
                    pygame.time.delay(50)
                    self.testPirate.setPosition((path[x],path[x+1]))
                    x+=2
                except IndexError:
                    self.testPirate.setPosition((treasureX,treasureY))
                    if self.testLandmark.getSearched() == False:
                        print "Treasure Acquired!"
                        self.inventory.addScore(100)
                    self.testLandmark.setSearched(True)
                    #self.testPirate.setHasReachedDestination(True)

            #re/draw the map
            self.map.drawMap(self.screen)

            #treasure spotter
            boundary = 1
            if self.testPirate.getGridPos()[0] <= self.testLandmark.getGridPos()[0]+boundary\
                and self.testPirate.getGridPos()[0] >= self.testLandmark.getGridPos()[0]-boundary\
                and self.testPirate.getGridPos()[1] <= self.testLandmark.getGridPos()[1]+boundary\
                and self.testPirate.getGridPos()[1] >= self.testLandmark.getGridPos()[1]-boundary:
                    self.land.append(self.testPirate.getGridPos())

            #add the score to the screen
            self.score = self.font.render("Score: "+str(self.inventory.dispScore()), 1, self.colour)
            self.screen.blit(self.score, (10, self.height-215))

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    window = Game()
   # window.playIntro()
    window.setup()
    window.loop()
