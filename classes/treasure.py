class treasure():
    def __init__(self,ID,found= True ):            #Properties of my class
        self.ID=ID
        self.found= found


    def isFound(self):                            #This returns values to the landmark class             
        if self.found== True:                     #to show the tresaure has been found and searched
            return treasure_found_serchead        
        else:
            return not_searched
            
        


    def Showing_message(self):                   #This shows a message that the treasure as been found
        if self.found== True:                    #when robot is present
            print "Treasure", self.ID, "Found"
        

        

                                         
     
test = treasure(12,True)
print test.found
found=True
test.Showing_message()
