import random
from myGamePlayer import *

class enemy:
    def __init__(self, health, armour, dmg, miss, crit, slain):
        self.health = health
        self.armour = armour
        self.dmg = dmg
        self.miss = miss
        self.crit = crit
        self.slain = slain
    
    def attack(self):
        dmg = 0
        dmg = random.randrange(self.dmg / 2, self.dmg)
        if random.randrange(1, 100) < self.crit:
            dmg *= 2
            print("*CRIT*")
        elif random.randrange(1, 100) < self.miss:
            dmg = 0
            print("*MISS*")
        return int(dmg)
    
    def block(self, playerDmg):
        dmg = playerDmg
        dmg -= int((playerDmg * (100 - self.armour)) / 100)
        return int(dmg)

    def heal(self):
        heal = random.randrange(5, 11)
        self.health += heal
        return int(heal)
    
    def decide(self):
        decision = random.randrange(1, 4)
        if self.health <= (self.health * 0.25):
            decision = 3
        return decision
