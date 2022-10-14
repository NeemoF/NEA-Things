class Character:
    def __innit__(self, playerClass = "mage", playerX = 0, playerY = 0, health = 100,):
        self.playerX =  playerX
        self.playerY = playerY
        self.health = health
        self.playerClass = self.playerClass(playerClass)
        self.ability1 = self.Ability1()
    
    # class playerClass():
    #     def __init__(self, Ability1, type):
    #         if self.type == "mage":
    #             Ability1.damage = 30
    #             Ability1.range = 100
    
    # class Ability1():
    #     def __init__(this):
    #         this.damage = 150
    #         this.range = 10