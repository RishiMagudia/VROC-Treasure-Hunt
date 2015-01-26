# Initialize attributes for Landmark.
    def __init__(self, name, size, pos, img, stat, desc):
        Base.__init__(self, name, size, pos, img, stat): #Initialize inherited attributes, from Base.
            self.decs = description
            self.name = name
            self.size = size
            self.position = pos
            self.image = img
            self.state = stat
            
    def __searched: #Method to check if Landmark searched, then effectivly hides the tresure if True. Variable is private, as it is only to be used in the Landmark class.

        for Treasure in Treasure_list:
            if self.position == Treasure:
                return True
            else:
                return False         
            

    def Treasure_present: #Method to check if treasure is present, by cross refrencing Landmark position with treasure position and seeing if Landmark already searched. 

        for Treasure in Treasure_list: #list of all locations of treasure objects
            if self.position == Treasure and __searched == False: #Using a list of treasure location, the current Landmark can be cross refrenced with all treasure location to see if treasure is present.
                return True
            else:
                return False
