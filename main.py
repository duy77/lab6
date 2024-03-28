
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name = "Hero", health = 100)
hero.equip(iron_sword)
enemy = Enemy(name ="enemy", health =100, weapon = short_bow)

while True:
    os.system("clear")
    hero.attack(enemy)
    enemy.attack(hero)
    
    hero.health_bar.draw()
    enemy.health_bar.draw()
    input()
   # print(f"health of {hero.name} : {hero.health}")
   # print(f"Health of {enemy.name} : {enemy.health}")
   # hero.drop()
   
   