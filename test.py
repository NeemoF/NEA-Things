class player:
    def __init__(self, name, type):
        self.name = name
        self.type= type
    
    def getName(self):
        print(self.name)

    def getType(self):
        print(self.type)
    
    def setName(self, newName):
        self.name = newName

object = player("Neema", "Mage")

thisDict = {
    "Name" : object.getName,
    "Two" : object.getType,
    "Three" : object.setName,
}

thisList = [
    object.getName,
    object.getType,
    object.setName
]

thisList[2]("James")
thisList[0]()

object.getName()