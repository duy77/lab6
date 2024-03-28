from character import Hero, Enemy
from weapon import Weapon
import os

#setup
healing_staff = Weapon("Healing Staff","magic", -3,0)
empty_handed = Weapon("Empty Handed", "dummy", 0, 0)

protagonist = Hero("Hero", 100)
protagonist.health_max = 100
ally = Enemy("Friendly enemy", 100, healing_staff)

protagonist.equip(empty_handed)
protagonist.health = 10


#game loop
while True:
    os.system("clear")

    protagonist.attack(ally)
    ally.attack(protagonist)

    protagonist.health_bar.draw()
    ally.health_bar.draw()

    input()