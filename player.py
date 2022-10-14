from random import randint
class Character():
    def __init__(self):
        self.playerX = 0
        self.playerY = 0
        self.health = 100
        self.playerClass = "" 
        self.alive = True
    
    class ability1():
        def __init__(this, playerClass):
            if playerClass == "Mage":
                this.damage = 15
                this.range = 20
            elif playerClass == "Warrior":
                this.damage = 20
                this.range = 5
            elif playerClass == "Archer":
                this.damage = 75
                this.range = 125
    
    class ability2():
        def __init__(this, playerClass):
            if playerClass == "Mage":
                this.damage = 105
                this.range = 5
            elif playerClass == "Warrior":
                this.damage = 130
                this.range = 5
            elif playerClass == "Archer":
                this.damage = 70
                this.range = 135
    
    class ability3():
        def __init__(this, playerClass):
            if playerClass == "Mage":
                this.damage = 113
                this.range = 104
            elif playerClass == "Warrior":
                this.damage = 127
                this.range = 5
            elif playerClass == "Archer":
                this.damage = 79
                this.range = 172

    class ability4():
        def __init__(this, playerClass):
            if playerClass == "Mage":
                this.damage = 102
                this.range = 103
            elif playerClass == "Warrior":
                this.damage = 133
                this.range = 143
            elif playerClass == "Archer":
                this.damage = 152
                this.range = 69

    def selectClass(self):
        check = False
        while check != True:
            chosenClass = input("Please enter Player Class from Archer, Mage and Warrior: ")
            chosenClass = chosenClass.capitalize()
            if chosenClass == "Warrior" or chosenClass == "Mage" or chosenClass == "Archer":
                self.playerClass = chosenClass
                self.ability1 = self.ability1(chosenClass)
                self.ability2 = self.ability2(chosenClass)
                self.ability3 = self.ability3(chosenClass)
                self.ability4 = self.ability4(chosenClass)
                check = True
    
    def passiveAbility(self):
        number = randint(0,4)
        if self.playerClass == "Mage":
            if number == 3:
                return "healPlayer"
        elif self.playerClass == "Warrior":
            if number == 3:
                return "damageEnemy"
        elif self.playerClass == "Archer":
            if number == 3:
                return "dodge"

    def playerMovement(self, key):
        if key == "w":
            self.playerY += 1
        elif key == "a":
            self.playerX -= 1
        elif key == "s":
            self.playerY -= 1
        elif key == "d":
            self.playerX += 1
    
    def abilityRangeVal(self, key):
        if key == "1":
            return self.ability1.range
        elif key == "2":
            return self.ability2.range
        elif key == "3":
            return self.ability3.range
        elif key == "4": 
            return self.ability4.range
    
    def abilityDamageVal(self, key):
        if key == "1":
            return self.ability1.damage
        elif key == "2":
            return self.ability2.damage
        elif key == "3":
            return self.ability3.damage
        elif key == "4": 
            return self.ability4.damage