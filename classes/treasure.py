class treasure():
    def __init__(self,ID,found= True ):
        self.ID=ID
        self.found= found


    def isFound(self):                                                  #This is used to see if the treausre is found
        print "no"
        

    
    def Showing_message(self):                                          #This shows a message saying the Treasure is found
        print "Treasure", ID, "Found"

        

                                         
     
test = treasure(12,True)
print test.found
test.Showing_message()
test.isFound()
