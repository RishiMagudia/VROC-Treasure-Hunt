class Landmark:
    
    def __init__(self, Postion, Image, Size, Description, Searched):
        self.Position = Postion
        self.Image = Image
        self.Size = Size
        self.Description = Description
        self.Searched = Searched

    def Display_is_landmark_searched(self):
        print "test"

    def Display_description(self):
        print "test"
    

test = Landmark(1,1,1,"test",True)

print test.Searched

test.Display_is_landmark_searched()

test.Display_description()
