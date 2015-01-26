class Map:
    
    #initializing variables
    def __init__(self):
        self.priority2()
        self.sList = []
        self.pList = []

    #blitting/printing the prioritized list of items    
    def drawMap(self,sList):
        running = True
        while running == True:
            for i in self.sList:
                name, coordiantes, priority = i
                for i in range(len(self.sList),0,1):
                    screen.blit(name,(coordinates))

    #prioritizing the list of unsorted images
    def prioritize(self,img_list):
        #unpackage the list of images, take out priority and store it in a list
        for n in img_list:
            pList.append(n[2])
            
        #sort the created list of priority numbers
        pList = sorted(pList)
        
        #compare all the priority numbers from pList to the unsorted img_list
        #and if prioritys mach add the package into the new sorted sList
        for i in range(len(pList)):
            for m in img_list:
                if m[2] == pList[i] and m not in self.sList:
                    self.sList.append(m)
