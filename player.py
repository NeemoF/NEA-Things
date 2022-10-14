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
                this.damage = 20
                this.range = 20
            elif playerClass == "Warrior":
                this.damage = 30
                this.range = 10
            elif playerClass == "Archer":
                this.damage = 10
                this.range = 30
    
    class ability2():
        def __init__(this, playerClass):
            if playerClass == "Mage":
                this.damage = 25
                this.range = 15
            elif playerClass == "Warrior":
                this.damage = 35
                this.range = 5
            elif playerClass == "Archer":
                this.damage = 20
                this.range = 35
    
    class ability3():
        def __init__(this, playerClass):
            if playerClass == "Mage":
                this.damage = 15
                this.range = 15
            elif playerClass == "Warrior":
                this.damage = 20
                this.range = 3
            elif playerClass == "Archer":
                this.damage = 3
                this.range = 20

    class ability4():
        def __init__(this, playerClass):
            if playerClass == "Mage":
                this.damage = 19
                this.range = 14
            elif playerClass == "Warrior":
                this.damage = 27
                this.range = 2
            elif playerClass == "Archer":
                this.damage = 200
                this.range = 100

    def showStats(self):
        print("X: " + str(self.playerX), "\nY: " + str(self.playerY), "\nHealth: " + str(self.health), "\nDamage: " + str(self.damage), "\nRange: " + str(self.range), "\nAlive: " + str(self.alive), "\nClass: " + str(self.playerClass))

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
    
    def abilityStats(self):
        print("Ability1 - Damage: " + str(self.ability1.damage), ", Range: " + str(self.ability1.range))
        print("Ability2 - Damage: " + str(self.ability2.damage), ", Range: " + str(self.ability2.range))
        print("Ability3 - Damage: " + str(self.ability3.damage), ", Range: " + str(self.ability3.range))
        print("Ability4 - Damage: " + str(self.ability4.damage), ", Range: " + str(self.ability4.range))