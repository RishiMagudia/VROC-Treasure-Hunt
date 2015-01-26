class Map:
    
    def __init__(self):
        # starting off the class
        self.priority2()
        self.sList = []
        self.pList = []
        
    def drawMap(self,sList):
        #drawing the map
        running = True
        while running == True:
            for i in self.sList:
                name, coordiantes, priority = i
                for i in range(len(self.sList),0,1):
                    screen.blit(name,(coordinates))
                    
    def prioritize(self,img_list):
        #sorting the images by priority number
        for n in img_list:
            pList.append(n[2])
        # sort the created list
        pList = sorted(pList)
        # compare the priority to the unsorted list and if prioritys mach
        # add the package into the new sorted list
        for i in range(len(pList)):
            for m in img_list:
                if m[2] == pList[i] and m not in self.sList:
                    self.sList.append(m)
