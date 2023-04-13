import random
from myGamePlayer import *
from myGameMenu import *
from myGameEnemy import *

def combat1(Player1, goblin1):
    while Player1.health > 0:
        os.system('cls')
        print("*" * 50)
        print("* Goblin" + " " * (37 - len(Player1.name)) + Player1.name + "    *")
        print("* Health: " + str(goblin1.health) + " " * (30 - len(str(goblin1.health)) - len(str(Player1.health))) + "Health: " + str(Player1.health) + " *")
        print("*" + " " * 48 + "*")
        print("* 1. Attack" + " " * 38 + "*")
        print("* 2. Block" + " " * 39 + "*")
        print("* 3. Heal" + " " * 40 + "*")
        print("*" * 50)
        chosen = False
        while not chosen:
            action = 0
            try:
                action = int(input("\nChoose your action: "))
                if action <= 0 or action > 3:
                    action = int("stop")
                chosen = True
            except Exception:
                print("Please choose one of the available options")
        print()
        dmg = 0
        dmg2 = 0
        block = 0
        heal = 0
        enemyDmg = 0
        match action:
            case 1:
                dmg = Player1.attack()
                print(Player1.name + " does " + str(dmg) + " damage to the goblin")
                if Player1.type == 4:
                    dmg2 = Player1.attack()
                    print(Player1.name + " does " + str(dmg2) + " damage to the goblin")
                print()
                if goblin1.health > 0:
                    decision = goblin1.decide()
                    match decision:
                        case 1:
                            enemyDmg = goblin1.attack()
                            print("The goblin does " + str(enemyDmg) + " to " + str(Player1.name))
                        case 2:
                            block = goblin1.block(dmg + dmg2)
                            print("The goblin blocks " + str(block) + " damage and takes " + str(dmg + dmg2 - block))
                        case 3:
                            heal = goblin1.heal()
                            print("The goblin heals " + str(heal) + " points of damage")
                    print()
                    goblin1.health -= dmg + dmg2 - block
                    Player1.health -= enemyDmg
                    if goblin1.health <= 0:
                        print(Player1.name + " slays Goblin 1")
                        goblin1.slain = True
                        Player1.numSlain += 1
                        print()

            case 2:
                decision = random.randrange(1, 3)
                match decision:
                    case 1:
                        enemyDmg = goblin1.attack()
                        block = Player1.block(enemyDmg)
                        print(Player1.name + " blocks " + str(block) + " damage and takes " + str(enemyDmg - block))
                        Player1.health -= (enemyDmg - block)
                    case 2:
                        heal = goblin1.heal()
                        print(Player1.name + " blocks while the goblin heals " + str(heal) + " points of damage")
                print()

            case 3:
                heal = Player1.heal()
                print(Player1.name + " heals " + str(heal) + " points of damage")
                decision = random.randrange(1, 3)
                print()
                match decision:
                    case 1:
                        enemyDmg = goblin1.attack()
                        print("The goblin does " + str(enemyDmg) + " damage to " + str(Player1.name))
                        Player1.health -= enemyDmg
                    case 2:
                        heal = goblin1.heal()
                        print("The goblin heals " + str(heal) + " points of damage")
                print()

        input("(Press ENTER to continue...)")

        if goblin1.slain:
            return True

        if Player1.health <= 0:
            playerDeath()
            return False


def combat2(Player1, goblin1, goblin2):

    while Player1.health > 0:
        os.system('cls')
        print("*" * 60)
        print("* Goblin 1" + " " * (13) + "Goblin 2" + " " * (24 - len(Player1.name)) + Player1.name + "    *")
        print("* Health: " + str(goblin1.health) + " " * (15 - len(str(goblin1.health)) - len(str(goblin2.health))) + "Health: " + str(goblin2.health) + " " * (17 - len(str(Player1.health))) + "Health: " + str(Player1.health) + " *")
        print("*" + " " * 58 + "*")
        print("* 1. Attack" + " " * 48 + "*")
        print("* 2. Block" + " " * 49 + "*")
        print("* 3. Heal" + " " * 50 + "*")
        print("*" * 60)

        chosen = False
        while not chosen:
            try:
                action = int(input("\nChoose your action: "))
                if action <= 0 or action > 3:
                    action = int("")
                chosen = True
            except Exception:
                print("Please choose one of the options above")
        print()

        match action:
            case 1:
                dmg = 0
                dmg2 = 0
                choice1 = 0
                choice2 = 0

                if Player1.type == 4:
                    print("You can attack twice\n")
                    print("First choice")
                if goblin1.health <= 0:
                    choice1 = 2
                if goblin2.health <= 0:
                    choice1 = 1
                while choice1 == 0:
                    try:
                        choice1 = int(input("Goblin 1 or 2: "))
                        if choice1 < 0 or choice1 > 2:
                            choice1 = int("stop")
                    except Exception:
                        print("Please choose from the available enemies")
                if Player1.type == 4:
                    if goblin1.health <= 0:
                        choice2 = 2
                    if goblin2.health <= 0:
                        choice2 = 1
                    while choice2 == 0:
                        try:
                            choice2 = int(input("\nGoblin 1 or 2: "))
                            if choice2 < 0 or choice2 > 2:
                                choice2 = int("stop")
                        except Exception:
                            print("Please choose from the available enemies")
                print()
                dmg = Player1.attack()
                match choice1:
                    case 1:
                        print(Player1.name + " does " + str(dmg) + " damage to Goblin 1")
                    case 2:
                        print(Player1.name + " does " + str(dmg) + " damage to Goblin 2")
                
                if Player1.type == 4:
                    print()
                    dmg2 = Player1.attack()

                match choice2:
                    case 1:
                        print(Player1.name + " does " + str(dmg2) + " damage to Goblin 1")
                    case 2:
                        print(Player1.name + " does " + str(dmg2) + " damage to Goblin 2")
                
                print()
                if goblin1.health > 0:
                    decision = goblin1.decide()
                    dmg3 = 0
                    if choice1 == 1:
                        dmg3 = dmg
                    if choice2 == 1:
                        dmg3 = dmg + dmg2
                    match decision:
                        case 1:
                            enemyDmg = goblin1.attack()
                            print("Goblin 1 does " + str(enemyDmg) + " damage to " + Player1.name)
                            goblin1.health -= dmg3
                            Player1.health -= enemyDmg
                        case 2:
                            block = goblin1.block(dmg3)
                            print("Goblin 1 blocks " + str(block) + " damage and takes " + str(dmg3 - block))
                            goblin1.health -= dmg3 - block
                        case 3:
                            heal = goblin1.heal()
                            print("Goblin 1 heals " + str(heal) + " points of damage but takes " + str(dmg3))
                            goblin1.health -= dmg3
                if goblin1.health <= 0 and not goblin1.slain:
                    goblin1.health = 0
                    goblin1.slain = True
                    print(Player1.name + " slays Goblin 1")
                    Player1.numSlain += 1

                print()
                if goblin2.health > 0:
                    decision2 = goblin2.decide()
                    dmg3 = 0
                    if choice1 == 2:
                        dmg3 = dmg
                    if choice2 == 2:
                        dmg3 = dmg + dmg2
                    match decision2:
                        case 1:
                            enemyDmg2 = goblin2.attack()
                            print("Goblin 2 does " + str(enemyDmg2) + " damage to " + Player1.name)
                            goblin2.health -= dmg3
                            Player1.health -= enemyDmg2
                        case 2:
                            block2 = goblin2.block(dmg3)
                            print("Goblin 2 blocks " + str(block2) + " damage and takes " + str(dmg3 - block2))
                            goblin2.health -= dmg3 - block2
                        case 3:
                            heal2 = goblin2.heal()
                            print("Goblin 2 heals " + str(heal2) + " points of damage but takes " + str(dmg3))
                            goblin2.health -= dmg3
                if goblin2.health <= 0 and not goblin2.slain:
                    goblin2.health = 0
                    goblin2.slain = True
                    print(Player1.name + " slays Goblin 2")
                    Player1.numSlain += 1

            case 2:
                enemyDmg = 0
                enemyDmg2 = 0

                print()
                if goblin1.health > 0:
                    decision = random.randrange(1, 3)
                    match decision:
                        case 1:
                            enemyDmg = goblin1.attack()
                            block = Player1.block(enemyDmg)
                            print(Player1.name + " blocks " + str(block) + " damage from Goblin 1 and takes " + str(enemyDmg - block))
                            Player1.health -= (enemyDmg - block)
                        case 2:
                            heal = goblin1.heal()
                            print(Player1.name + " blocks while Goblin 1 heals " + str(heal) + " points of damage")
                
                print
                if goblin2.health > 0:
                    decision2 = random.randrange(1, 3)
                    match decision2:
                        case 1:
                            enemyDmg2 = goblin2.attack()
                            block2 = Player1.block(enemyDmg2)
                            print(Player1.name + " blocks " + str(block2) + " damage from Goblin 2 and takes " + str(enemyDmg2 - block2))
                            Player1.health -= (enemyDmg2 - block2)
                        case 2:
                            heal2 = goblin2.heal()
                            print(Player1.name + " blocks while Goblin 2 heals " + str(heal2) + " points of damage")
            
            case 3:
                heal = Player1.heal()

                print()
                if goblin1.health > 0:
                    decision = random.randrange(1, 3)
                    match decision:
                        case 1:
                            enemyDmg = goblin1.attack()
                            print("Goblin 1 does " + str(enemyDmg) + " damage to " + Player1.name)
                            Player1.health -= enemyDmg
                        case 2:
                            heal = goblin1.heal()
                            print("Goblin 1 heals " + str(heal) + " points of damage")
                
                print()
                if goblin2.health > 0:
                    decision2 = random.randrange(1, 3)
                    match decision2:
                        case 1:
                            enemyDmg2 = goblin2.attack()
                            print("Goblin 2 does " + str(enemyDmg2) + " to " + Player1.name)
                            Player1.health -= enemyDmg2
                        case 2:
                            heal2 = goblin2.heal()
                            print("Goblin 2 heals " + str(heal2) + " points of damage")
    
        input("\n(Press ENTER to continue...)")

        if goblin1.slain and goblin2.slain:
            return True
        
        if Player1.health <= 0:
            playerDeath()
            return False
                        