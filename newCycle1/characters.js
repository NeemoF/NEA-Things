export class Player{
  constructor() {
    this.playerX = 12;
    this.playerY = 12;
    this.health = 100;
    this.playerClass = "";
    this.alive = true
  }
  
  calcLocation() {
    return this.playerX + this.playerY*25;
  }
}

export class Enemy{
  constructor() {
    this.enemyX = 0;
    this.enemyY = 0;
    this.damage = 0;
    this.health = 0;
    this.distance = 999;
    this.alive = true;
  }
  
  createEnemy() {
    while (this.enemyX == 12 && this.enemyY == 12) {
      this.enemyX = Math.floor(Math.random() * 25);
      this.enemyY = Math.floor(Math.random() * 25);
    }

    this.enemyX = Math.floor(Math.random() * 25);
    this.enemyY = Math.floor(Math.random() * 25);
    this.damage = Math.floor(Math.random() * 10) + 10;
    this.health = Math.floor(Math.random() * 20) + 80;
  }

  calcLocation() {
    return this.enemyX + this.enemyY*25;
  }
  
}