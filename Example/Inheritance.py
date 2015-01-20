class pet:
    def __init__(self, legs, size,):       #intialize pet class  
        self.legs = legs
        self.size = size
    
    def alot_of_legs(self):                #method for number of legs for pet class
        if self.legs == 4:
            print "Normal amount of legs"
        if self.legs > 4:
            print "Large amount of legs"
        if self.legs < 4:
            print "Small amount of legs"

    def size_of_pet(self):                  #method for size of pet for pet class
        if self.size == "big":
            print "big"
        if self.size == "medium":
            print "medium"
        if self.size == "small":
            print "small"

            

class dog(pet):
    def __init__(self, legs, size, job, snout_length):      #intialize dog class. This include the baseclass and subclass attributes.
        pet.__init__( self, legs, size)              #intializing the baseclass from the subclass with the baseclass used as an argument.
        self.job = job                                      #defined subclass arguments 
        self.snout_length = snout_length


    def size_of_snout(self):                                #method for size of snout for dog
        
        if self.snout_length >= 4:
            print "That's a big snout"
        elif self.snout_length < 4 and self.snout_length > 2:
            print "That's a normal snout"
        else:
            print "That's a small snout"
            
rex = dog(4, "big", "fire dog",6 )

print rex.job

rex.alot_of_legs()

rex.size_of_snout()

rex.size_of_pet()
