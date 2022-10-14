from random import randint
import math
class Enemy():
    def __init__(self):
        self.health = 0
        self.damage = 0
        self.locationX = 0
        self.locationY = 0
        self.distance = 999
    
    def createEnemy(self):
        self.health = randint(50, 200)
        self.damage = randint(10, 20)
        while self.locationX == 0 and self.locationY == 0:
            self.locationX = randint(-25, 25)
            self.locationY = randint(-25, 25)
    
    def updateDistance(self, character):
        dx = self.locationX - character.playerX
        dy = self.locationY - character.playerY
        self.distance = round(math.sqrt(dx**2 + dy**2), 0)