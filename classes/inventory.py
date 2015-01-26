class Inventory:

    #initializing variables
    def __init__(self):
        self.itemList = []
        self.score = 0

    #function for adding treasures to a list
    def addTreasure(self,treasure):
        self.itemList.append(treasure)

    #adding up the total score
    def addScore(self,score):
        self.score += score
        
    #return the list of items in the inventory
    def dispTrsr(self):
        return self.itemList

    #return the total score
    def dispScore(self):
        return self.score
