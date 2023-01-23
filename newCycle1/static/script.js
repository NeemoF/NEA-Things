import { Player, Enemy } from "./characters.js";

document.addEventListener("DOMContentLoaded", () =>{
    const grid = document.getElementById("grid")
    const healthBarContainer = document.getElementById("healthBar")
    const combatScreen = document.getElementById("combat")
    const width = 25
    const height = 25
    const maxHealth = 100
    var combatBackground = 'url("Images/combatScreens/combat4-4.png")'
    var screenWidth = window.innerWidth
    var screenHeight = window.innerHeight
    var player = new Player()
    var squaresLocation = player.calcLocation()
    var enemiesArray = []
    var squares = []
    var currentEnemy

    const mouse = {
        x: screenWidth/2,
        y: screenHeight/2,
        click: false
    }

    function createGrid(){
        for (let i=0; i<625; i++){
            const box = document.createElement("div")
            grid.appendChild(box)
        }
        
        squares = document.querySelectorAll(".flex div")
    }

    function onStart(){
        createGrid()
        squares[squaresLocation].classList.add("player")
        createEnemies()
        update()
    }

    function createEnemy(i){
        enemiesArray.push(new Enemy())
        enemiesArray[i].createEnemy()
        var random = Math.random() <= 0.5 ? "enemy1" : "enemy2"
        squares[enemiesArray[i].calcLocation()].classList.add(random)
    }

    function createEnemies(){
        for (let i=0; i<4; i++){
            createEnemy(i)
        }
    }

    function update(){
        squares[squaresLocation].classList.remove("player");
        squaresLocation = player.calcLocation()
        
        if (squares[squaresLocation].classList.contains("enemy1") || squares[squaresLocation].classList.contains("enemy2")){            
            combat()
        }

        squares[squaresLocation].classList.add("player")
        healthBar()
    }

    function combat(){
        combatScreen.style.background= "white";
        combatScreen.style.backgroundImage = combatBackground;   
        document.removeEventListener("keydown", playerMovemove)     
        var enemyY = Math.floor(squaresLocation / width)
        var enemyX = squaresLocation % width

        enemiesArray.forEach(enemy => {
            if (enemy.enemyX == enemyX && enemy.enemyY == enemyY){
                currentEnemy = enemy
                document.addEventListener("click", playerAttack)
                playerAttack()
            }
        })
    }

    function playerAttack() { // 593 625
        console.log(mouse.y)
        var enemyHealthPercentage = (currentEnemy.health/maxHealth * 100).toString()
        var playerHealthPercentageInt = (player.health/maxHealth * 100).toString()

        var bar1 = Math.floor(playerHealthPercentageInt/33) + 1
        var bar2 = Math.floor(enemyHealthPercentage/25)
        combatBackground = 'url(static/Images/combatScreens/combat' + bar1 + '-' + bar2 + '.png)'
        combatScreen.style.backgroundImage= combatBackground
        
        var random = Math.floor(Math.random() * 4)
        if (random != 0){
            if (player.health > 0 && currentEnemy.health > 0){
                if (mouse.x > 263  && mouse.x < 509 && mouse.y > 593 && mouse.y < 625){
                    currentEnemy.health -= 10
                } else if (mouse.x > 516 && mouse.x < 768 && mouse.y > 593 && mouse.y < 625){
                    currentEnemy.health -= 10
                } else if (mouse.x > 790 && mouse.x < 1022 && mouse.y > 593 && mouse.y < 625){
                    currentEnemy.health -= 10
                } else if (mouse.x > 1034 && mouse.x < 1278 && mouse.y > 593 && mouse.y < 625){
                    currentEnemy.health -= 10
                }
            }
        }   else {
            player.health -= currentEnemy.damage
        }
        
        if (currentEnemy.health <= 0 || player.health <= 0){
            combatScreen.style.background= "transparent";
            combatScreen.style.backgroundImage = 'none';
            if (player.alive === true){
                document.addEventListener("keydown", playerMovemove)
            }

            document.removeEventListener("click", playerAttack)
            enemiesArray.splice(enemiesArray.indexOf(currentEnemy), 1)
            squares[squaresLocation].classList.remove("enemy1")
            squares[squaresLocation].classList.remove("enemy2")
            createEnemy(3)
            mouse.x = 0
        }
        healthBar()
    }


    function healthBar(){
        var playerHealthPercentage = (player.health/maxHealth * 100).toString()
        healthBarContainer.style.background = "linear-gradient(to right, red " + playerHealthPercentage + "%, white " + playerHealthPercentage + "%)"

        if (player.health <= 0){ 
            document.removeEventListener("keydown", playerMovemove)
            player.alive=false
            setTimeout(function(){ window.alert("You died!") }, 1)
        }
    }

    function playerMovemove(e){
        switch(e.keyCode){
            case 65:
            case 37 :
                if (squaresLocation % 25 !=0 ){
                    player.playerX -= 1
                    update()
                }
                break

            case 87:
            case 38:
                if (squaresLocation - width >= 0){
                    player.playerY -= 1
                    update()
                }
                break
            case 68:
            case 39:
                if (squaresLocation % width != 24){
                    player.playerX += 1
                    update()
                }
                break
            
            case 83:
            case 40:
                if (squaresLocation + width <= 624){
                    player.playerY += 1
                    update()
                }
        }
    }
    
    combatScreen.addEventListener("mousedown", function(event) {
        mouse.click = true
        mouse.x = event.x
        mouse.y = event.y 
    })

    onStart()
    document.addEventListener("keydown", playerMovemove)

    window.addEventListener("keydown", function(e) { // space and arrow keys 
        if([32, 37, 38, 39, 40].indexOf(e.keyCode) > -1) { e.preventDefault(); } }, false);
})
