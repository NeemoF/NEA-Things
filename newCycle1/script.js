import { Player, Enemy } from "./characters.js";


document.addEventListener("DOMContentLoaded", () =>{
    const grid = document.getElementById("grid") // get the grid
    const healthBarContainer = document.getElementById("healthBar")
    const width = 25
    const height = 25
    const maxHealth = 100
    var player = new Player()
    var squaresLocation = player.calcLocation()
    var enemiesArray = []
    var squares = []

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
        squares[squaresLocation].classList.remove("player")
        squaresLocation = player.calcLocation()
        
        if (squares[squaresLocation].classList.contains("enemy1") || squares[squaresLocation].classList.contains("enemy2")){
            var enemyY = Math.floor(squaresLocation / width)
            var enemyX = squaresLocation % width
            enemiesArray.forEach(enemy => {
                if (enemy.enemyX == enemyX && enemy.enemyY == enemyY){
                    enemy.health -= 1000
                    if (enemy.health <= 0){
                        enemiesArray.splice(enemiesArray.indexOf(enemy), 1)
                        squares[squaresLocation].classList.remove("enemy1")
                        squares[squaresLocation].classList.remove("enemy2")
                        createEnemy(3)
                    }
                }
            })
            player.health -= 10
        }
        squares[squaresLocation].classList.add("player")
        
        setTimeout(healthBar, 1)
    }

    function healthBar(){
        var playerHealthPercentage = (player.health/maxHealth * 100).toString()
        healthBarContainer.style.background = "linear-gradient(to right, red " + playerHealthPercentage + "%, white " + playerHealthPercentage + "%)"

        if (player.health <= 0){ 
            
            document.removeEventListener("keydown", playerMovemove)
            setTimeout(function(){ window.alert("You died!") }, 1)
        }
    }

    function playerMovemove(e){
        switch(e.keyCode){
            case 37:
                if (squaresLocation % 25 !=0 ){
                    player.playerX -= 1
                    update()
                }
                break

            case 38:
                if (squaresLocation - width >= 0){
                    player.playerY -= 1
                    update()
                }
                break

            case 39:
                if (squaresLocation % width != 24){
                    player.playerX += 1
                    update()
                }
                break

            case 40:
                if (squaresLocation + width <= 624){
                    player.playerY += 1
                    update()
                }
        }
    }

    onStart()
    document.addEventListener("keydown", playerMovemove)

    window.addEventListener("keydown", function(e) { // space and arrow keys 
        if([32, 37, 38, 39, 40].indexOf(e.keyCode) > -1) { e.preventDefault(); } }, false);
})