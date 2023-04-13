# This is the supporting file
import os
import random
from myGameEnemy import *

class Player:
    def __init__(self, name, type, armour, crit, weaponDmg, miss, health, numSlain, currentChp):
        self.name = name
        self.type = type
        self.armour = armour
        self.crit = crit
        self.weaponDmg = weaponDmg
        self.miss = miss
        self.health = health
        self.numSlain = numSlain
        self.currentChp = currentChp

    def getName(self):
        while self.name == "":
            self.name = input("\nWhat is your name?: ")
            if self.name == "":
                print("\nCome on, I gotta know your name if I am going to narrate this")

    def getChar(self):
        if self.weaponDmg == 0:
            print("\nHello " + self.name + ", my name is Clyde")
            print("Welcome to my game...\n")
            print("Now I need you to choose an archetype.")
            print("It is simple because I am not very smart.\n")
            print("What type of warrior will you be?\n")
            print("1. Barbarian (Med Armour, Med crit chance)")
            print("2. Knight (High Armour, Low crit chance)")
            print("3. Assassin (Low Armour, High crit chance)")
            print("4. Monk (Low Armour, Low crit chance, attacks twice each turn)")

            chosenType = False

            while not chosenType:
                try:
                    choice = int(input("\nWhich do you choose? (Pick a number): "))
                    if choice <= 0 or choice > 4:
                        choice = int("stop")
                    chosenType = True
                except Exception:
                    print("\nYou gotta choose something...")

            match choice:
                case 1:
                    print("\nOk, Barbarians are sorta fun I think...")
                    self.type = 1
                    self.crit = 10
                    self.armour = 30
                case 2:
                    print("\nKnight huh? Nothing wrong with old faithful")
                    self.type = 2
                    self.crit = 5
                    self.armour = 45
                case 3:
                    print("\nAssassin...interesting, Hopefully you can make it work")
                    self.type = 3
                    self.crit = 15
                    self.armour = 15
                case 4:
                    print("\nMonk... Devout and Resourceful")
                    self.type = 4
                    self.crit = 10
                    self.armour = 15
            input("(Press ENTER to continue...)")
            os.system('cls')

            print("\nNext... choose your starting weapon\n")
            print("1. Broadsword (20 dmg, 12% chance miss)")
            print("2. Short Knife (8 dmg, 3% chance miss)")
            print("3. Hand axe (16 dmg, 9% chance miss)")
            print("4. Bowstaff (12 dmg, 6% chance miss)\n")

            chosenWpn = False
            while not chosenWpn:
                try:
                    choice = int(input("\nPick your poison (choose a number): "))
                    if choice <= 0 or choice > 4:
                        choice = int("stop")
                    chosenWpn = True
                except Exception:
                    print("\nYou shouldn't go empty handed...")

            match choice:
                case 1:
                    print("\nStrong but heavy, hard to wield")
                    self.weaponDmg = 20
                    self.miss = 12
                case 2:
                    print("\nQuick and clean, yet doesnt cut too deep")
                    self.weaponDmg = 8
                    self.miss = 3
                case 3:
                    print("\nIndustry Standard, if you're a lumberjack")
                    self.weaponDmg = 16
                    self.miss = 9
                case 4:
                    print("\nBowstaff is neat")
                    self.weaponDmg = 12
                    self.miss = 6

            input("(Press ENTER to continue...)")
            os.system('cls')
    
    def attack(self):
        dmg = random.randrange((self.weaponDmg * 0.75), self.weaponDmg)
        if random.randrange(1, 100) < self.crit:
            print("*CRIT*")
            dmg *= 2
        elif random.randrange(1, 100) < self.miss:
            print("*MISS*")
            dmg = 0
        return int(dmg)
    
    def block(self, enemyDmg):
        block = (enemyDmg * ((100 - self.armour) / 100))
        return int(block)
    
    def heal(self):
        if self.health <= (150 / 3):
            heal = random.randrange(int(150 * 0.10), int(150 * 0.20))
        else:
            heal = random.randrange(int(150 * 0.05), int(150 * 0.15))
        self.health += heal
        return int(heal)
