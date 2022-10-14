from player import Character
from enemy import Enemy
from random import randint

#Subroutine to handle the player input such as move, attack or end game
def playerRequest(key, character, array):
    movement = ["w", "a", "s", "d"]
    abilities = ["1", "2", "3", "4"]
    if key in movement:
        character.playerMovement(key)
        print(character.playerX, character.playerY)
        return True
    elif key in abilities:
        rangeVal = character.abilityRangeVal(key)
        for x in range(4):
            if array[x].distance <= rangeVal:
                combat(character, array[x], array)
                break
        return True
    elif key == "end":
        return False
    else:
        return True

#Update once per cycle to keep distances updated and check player location
def checkLocation(array, character):
    for x in range(4):
        if character.playerX == array[x].locationX and character.playerY == array[x].locationY:
            #if the player lands on an enemy, it'll start an attack
            print("Combat!")
            combat(character, array[x], array)

# Called when player enters combat
def combat(character, enemy, array):
    wonFight = False
    while character.alive and wonFight != True:
        passiveAbility = character.passiveAbility()
        eAttack = randint(0,4)
        if eAttack == 3 and passiveAbility != "dodge":
            character.health -= enemy.damage
            print("Your Health = " + str(character.health) + "\n")
        else:
            playerAttack(enemy, character, passiveAbility)
        
        if character.health <= 0:
            character.alive = False
        elif enemy.health <= 0:
            replaceEnemy(enemy, array)
            for x in range(4):
                print(array[x].locationX, array[x].locationY)
            wonFight = True
            print("Player Health = " + str(character.health))

def update(array, character):
    for x in range(4):
        array[x].updateDistance(character)
        print("Enemy " + str(x+1), "- Distance: " + str(array[x].distance))
    checkLocation(array, character)

#player uses an attack
def playerAttack(enemy, character, passive):
    playerAction = input("Enter Ability: ")
    if passive == "damageEnemy":
        damage = 1.25*abilityDamage(playerAction, character)
    elif passive == "healPlayer":
        damage = abilityDamage(playerAction, character)
        character.health += 10
    else:
        damage = abilityDamage(playerAction, character)
    enemy.health -= damage
    print("Enemy Health = " + str(enemy.health)+ "\n")

def abilityDamage(playerAction, character):
    abilities = ["1","2","3","4"]
    check = False
    while check != True:
        if playerAction in abilities:
            check = True
        else:
            playerAction = input("please try again: ")
    return character.abilityDamageVal(playerAction)
    
#replaces enemy, when enemy dies
def replaceEnemy(enemy, array):
    array.remove(enemy)
    array.append(Enemy())
    array[3].createEnemy()

# Create 4 Enemies
enemiesArray = []
for x in range(4):
    enemiesArray.append(Enemy())
    enemiesArray[x].createEnemy()
    #print(  "Enemy " + str(x+1), 
    #        "- LocationX: " +str(enemiesArray[x].locationX), 
    #        ", LocationY: " + str(enemiesArray[x].locationY),)

#create character and Set the class
character = Character()
character.selectClass()
#character.showStats()
character.abilityStats()


#Run the game
running = True
while running and character.alive:
    playerAction = input("Enter Command: ")
    running = playerRequest(playerAction, character, enemiesArray)
    update(enemiesArray, character)

