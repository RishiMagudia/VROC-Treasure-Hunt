import pygame, random, time

#import team's objects
import classes as c


ENABLE_GRID = False
ENABLE_ROBOT2 = False

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
        self.walls = []
        self.listOfLandmarks = []
        self.landmarkCounter = 0
        self.treasures = []
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
        self.pathfind2 = c.AStar()
        self.testPirate = c.robot()

        self.treasureText = c.Treasure()

        self.testPirate.setImage("images/pirate.png")
        self.testPirate.setSize(1)
        self.testPirate.setPosition((2, 15))
        self.loadup.append((self.testPirate, 1))

        if ENABLE_ROBOT2 == True:
            self.testPirate2 = c.robot()
            self.testPirate2.setImage("images/pirate.png")
            self.testPirate2.setSize(1)
            self.testPirate2.setPosition((4,15))
            self.loadup.append((self.testPirate2,1))

        self.testLandmark = c.Landmark()
        self.testLandmark.setImage("images/Hut_treasure.png")
        self.testLandmark.setSize(5)
        self.testLandmark.setPosition((0,1))
        self.listOfLandmarks.append(self.testLandmark)
        self.loadup.append((self.testLandmark, 2))

        self.testLandmark2 = c.Landmark()
        self.testLandmark2.setImage("images/Sunken ship_treasure.png")
        self.testLandmark2.setSize(5)
        self.testLandmark2.setPosition((13,1))
        self.listOfLandmarks.append(self.testLandmark2)
        self.loadup.append((self.testLandmark2,2))

        self.testLandmark3 = c.Landmark()
        self.testLandmark3.setImage("images/Big island_treasure.png")
        self.testLandmark3.setSize(13)
        self.testLandmark3.setPosition((19,-2))
        self.loadup.append((self.testLandmark3,2))

        self.testLandmark5 = c.Landmark()
        self.testLandmark5.setImage("images/Lighthouse_treasure.png")
        self.testLandmark5.setSize(7)
        self.testLandmark5.setPosition((16,11))
        self.listOfLandmarks.append(self.testLandmark5)
        self.loadup.append((self.testLandmark5,2))

        self.testLandmark6 = c.Landmark()
        self.testLandmark6.setImage("images/Treasure chest.png")
        self.testLandmark6.setSize(3)
        self.testLandmark6.setPosition((28,8))
        self.listOfLandmarks.append(self.testLandmark6)
        self.loadup.append((self.testLandmark6, 2))

        self.testLight = c.trafficLights()
        self.testLight.setImage("images/Whale.png")
        self.testLight.setSize(3)
        self.testLight.setPosition((25, 8))
        self.loadup.append((self.testLight, 2))

        for i in self.listOfLandmarks:
            print i.getGridPos(), " <-- landmark"


        #pirate's start point
        self.pier = c.Landmark()
        self.pier.setImage("images/Pier.png")
        self.pier.setSize(9)
        self.pier.setPosition((-1, 11))
        #self.listOfLandmarks.append(self.pier)
        self.loadup.append((self.pier, 2))

        #pirate end point
        self.endPoint = c.Landmark()
        self.endPoint.setPosition((1,13))
        self.listOfLandmarks.append(self.endPoint)

        self.obs = c.Landmark()
        self.obs.setImage("images/Small island.png")
        self.obs.setSize(2)

        self.map.prioritize(self.loadup)

        #set amount of treasures
        self.trsr_amount = random.randint(1, len(self.listOfLandmarks))

        #choose a landmark(s) for the treasure
        lm = [i.getGridPos() for i in self.listOfLandmarks]
        while len(self.treasures) < self.trsr_amount:
            t = random.choice(lm)
            if t not in self.treasures and t != (1, 13) and t != self.pier.getGridPos() and t not in self.land:
                self.treasures.append(t)

        print self.treasures, " <-- treasures"

        #generating obstacles, aka the map structure
        while len(self.land) < 15:
            xRandom = random.randint(4,10)
            yRandom = random.randint(4,6)
            if (xRandom, yRandom) not in self.walls:
                self.land.append((xRandom, yRandom))
                self.walls.append((xRandom, yRandom))
                self.walls.append((xRandom+1, yRandom))
                self.walls.append((xRandom, yRandom+1))
                self.walls.append((xRandom+1, yRandom+1))

            xRandom = random.randint(10,20)
            yRandom = random.randint(6,12)
            if (xRandom, yRandom+3) or (xRandom, yRandom) not in self.walls:
                self.land.append((xRandom, yRandom))
                self.walls.append((xRandom, yRandom))
                self.walls.append((xRandom, yRandom+1))
                self.walls.append((xRandom+1, yRandom+1))

            xRandom = random.randint(20,28)
            yRandom = random.randint(12,12)
            if (xRandom, yRandom) or (xRandom, yRandom) not in self.walls:
                self.land.append((xRandom, yRandom))
                self.walls.append((xRandom, yRandom))
                self.walls.append((xRandom, yRandom+1))
                self.walls.append((xRandom+1, yRandom+1))

        print 'obs generated'

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


    def callMsg(self):
        self.treasureText.showMessage(self.screen, 'Treasure Found',(10,10))
        


    def loop(self):
        """
            infinite loop to keep the images updating and moving
        """
        st = time.time()
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

            #working traffic light timer
            if time.time() - st > 3.0:
                st = time.time()
                self.trafficLight.rotateColour()

            #need to incorporate boundary search 
            #while self.testLight.getColour() == self.testLight.red and self.testLight.getGridPos() == self.testPirate.getGridPos():
                    #print "it's red"

            if self.testPirate.getHasReachedDestination() == True:
                self.callMsgStatus = True
                pygame.time.delay(1000)
                self.testPirate.setHasReachedDestination(False)
                #apply next treasure to pathfind to
                try:
                    currentTreasure = self.listOfLandmarks[self.landmarkCounter]
                    tempcood = currentTreasure.getGridPos()
                    treasureX = tempcood[0] +2
                    treasureY = tempcood[1] +1
                    self.landmarkCounter+=1
                except IndexError:
                    print ''
                    if self.trsr_amount == 0:
                        print "Game Over!"
                tempcood = self.testPirate.getGridPos()
                pirateX = tempcood[0]
                pirateY = tempcood[1]
                self.pathfind.init_grid(treasureX,treasureY,pirateX,pirateY,self.walls) #start cood and end cood + walls
                self.pathfind.algorithm()
                path = self.pathfind.getPath()
                x=0
            else:
                #traverse the path until destination is reached
                try:
                    #print self.testPirate.getPosition()
                    if self.testPirate.getPosition()[0] < path[x]*40:
                        #increment x cor
                        self.testPirate.setNPos((self.testPirate.getPosition()[0]+self.testPirate.getVelocity(),path[x+1]*40))
                    if self.testPirate.getPosition()[0] > path[x]*40:
                        #decrease x cor
                        self.testPirate.setNPos((self.testPirate.getPosition()[0]-self.testPirate.getVelocity(),path[x+1]*40))
                    if self.testPirate.getPosition()[1] < path[x+1]*40:
                        #increment y cor
                        self.testPirate.setNPos((path[x]*40,self.testPirate.getPosition()[1]+self.testPirate.getVelocity()))
                    if self.testPirate.getPosition()[1] > path[x+1]*40:
                        #decrease y cor
                        self.testPirate.setNPos((path[x]*40,self.testPirate.getPosition()[1]-self.testPirate.getVelocity()))

                    if self.testPirate.getPosition() == ((path[x]*40,path[x+1]*40)):
                        x+=2

                except IndexError:
                    self.testPirate.setPosition((treasureX,treasureY))
                    if currentTreasure.getSearched() == False:
                        if currentTreasure.getGridPos() in self.treasures:
                            self.inventory.addScore(random.randint(100, 1000))
                            self.trsr_amount -= 1
                            self.callMsg()
                            #currentTreasure shows message of the tresure
                            #tre = self.font.render("TREASURE ACQUIRED", 1, self.colour)
                            #self.screen.blit(tre, (10, 10))
                    currentTreasure.setSearched(True)
                    self.testPirate.setHasReachedDestination(True)

            #re/draw the map
            self.map.drawMap(self.screen)

            #add the "inventory" to the screen
            self.score = self.font.render("Score: "+str(self.inventory.dispScore()), 1, self.colour)
            self.txtTA = self.font.render("Treasures Left: "+str(self.trsr_amount), 1, self.colour)
            self.screen.blit(self.score, (10, self.height-220))
            self.screen.blit(self.txtTA, (10, self.height-240))
            
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)
            
            for i in range(len(self.loadup)):
                if self.landmark.Searched(SearchedLandmarkList[i]) == self.testLandmark:
                    self.testLandmark.setImage("images/Hut.png")
                if self.landmark.Searched(SearchedLandmarkList[i]) == self.testLandmark:
                    self.testLandmark.setImage("images/Sunken ship.png")
                if self.landmark.Searched(SearchedLandmarkList[i]) == self.testLandmark:
                    self.testLandmark.setImage("images/Big island.png")
                if self.landmark.Searched(SearchedLandmarkList[i]) == self.testLandmark:
                    self.testLandmark.setImage("images/Lighthouse.png")
                if self.landmark.Searched(SearchedLandmarkList[i]) == self.testLandmark:
                    self.testLandmark.setImage(none)
if __name__ == "__main__":
    window = Game()
   # window.playIntro()
    window.setup()
    window.loop()
