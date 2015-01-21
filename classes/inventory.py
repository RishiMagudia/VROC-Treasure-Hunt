class Inventory:

    def __init__(self):
        self.treasures = []
        self.score = 0

    def addTreasure(self,treasure):
        self.itemList.append(treasure)

    def addScore(self,score):
        self.score += score
        
    def dispTrsr(self):
        return self.treasure

    def dispScore(self):
        return self.score
