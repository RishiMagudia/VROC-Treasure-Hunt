class Map:
    
    #initializing variables
    def __init__(self):
        self.sList = []
        self.pList = []

    #blitting/printing the prioritized list of items    
    def drawMap(self, screen):
        for m in range(len(self.sList), 0, -1):
            img = self.sList[m-1].getImage()
            pos = self.sList[m-1].getPosition()
            screen.blit(img, pos)

    #prioritizing the list of unsorted images
    def prioritize(self, img_list):
        #unpackage the list of images, take out priority and store it in a list
        for n in img_list:
            self.pList.append(n[1])
            
        #sort the created list of priority numbers
        pList = sorted(self.pList)
        
        #compare all the priority numbers from pList to the unsorted img_list
        #and if prioritys mach add the package into the new sorted sList
        for i in range(len(pList)):
            for m in img_list:
                if m[1] == pList[i] and m not in self.sList:
                    self.sList.append(m[0])
