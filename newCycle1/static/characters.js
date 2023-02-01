export class Player{
  constructor() {
    this.LocationX = 12;
    this.LocationY = 12;
    this.health = 100;
    this.damage = 10;
    this.playerClass = "";
    this.AccountType = "";
    this.alive = true
    this.Password = "";
  }
  
  calcLocation() {
    return this.LocationX + this.LocationY*25;
  }

  convertToJSON() {
    var dict = {}
    dict["Password"] = this.Password;
    dict["AccountType"] = this.AccountType;
    dict["LocationX"] = this.LocationX;
    dict["LocationY"] = this.LocationY;
    return dict;
  }
}

export class Enemy{
  constructor() {
    this.enemyX = 12;
    this.enemyY = 12;
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

    this.damage = Math.floor(Math.random() * 10) + 10;
    this.health = Math.floor(Math.random() * 20) + 80;
  }

  calcLocation() {
    return this.enemyX + this.enemyY*25;
  }
  
}