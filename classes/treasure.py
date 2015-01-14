class treasure():
    def __innit__(self,ID,found= True):
        self.ID=ID
        self.found= found


    def isFound(self):                                           #see if the treasure has been found
        return self.found
        


    def ShowMessage(self):                                      #displaying message if robot finds the tresuare 
        print "Treasure",self.ID, "Found" 
