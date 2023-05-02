import os
import keyboard
import json
import time
import pygame
from pygame.locals import *

def pauseGame(gameWindow, font1, Player1, clock):
       exit() 

def playerDeath():
    os.system('cls')
    print("\nYou have taken one too many hits... You fade away into the dark...")
    input("(Press ENTER to continue...)")

def saveGame(Player1):
    os.system('cls')
    print("Would you like to save your progress?\n")
    choice = 0
    chosen = False
    while not chosen:
        try:
            choice = int(input("1. Yes\n2. No\n\nChoose your action: "))
            if choice <= 0 or choice > 2:
                choice = int("stop")
            chosen = True
        except Exception:
            print("\nPlease choose one of the available options...")
    
    if choice == 1:
        loadNames = [""] * 4
        loadChp = [""] * 4
        loadType = [""] * 4
        for x in range(1, 5, 1):
            filePath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame" + str(x) + ".txt"
            try:
                with open(filePath, "r") as file:
                    fileList = json.loads(file.read())
                    z = 0
                    for y in fileList:
                        if z == 0:
                            loadNames[x - 1] = y
                        elif z == 1:
                            loadType[x - 1] = y
                        elif z == 8:
                            loadChp[x -1] = y
                        z = z + 1
            except Exception:
                print("Error retrieving data from loading files")
            
        for x in range(4):
            match loadType[x]:
                case 1:
                    loadType[x] = "Barbarian"
                case 2:
                    loadType[x] = "Knight"
                case 3:
                    loadType[x] = "Assassin"
                case 4:
                    loadType[x] = "Monk"

        saveSlot = 0
        overwrite = False
        while overwrite == False:
            os.system('cls')
            print("Which save slot would you like to save to?")
            print("\n1. Slot 1 - Name: " + loadNames[0] + " " * (10 - len(loadNames[0])) + "Type: " + loadType[0] + " " * (12 - len(loadType[0])) + "Chapter: " + str(loadChp[0]))
            print("\n1. Slot 2 - Name: " + loadNames[1] + " " * (10 - len(loadNames[1])) + "Type: " + loadType[1] + " " * (12 - len(loadType[1])) + "Chapter: " + str(loadChp[1]))
            print("\n1. Slot 3 - Name: " + loadNames[2] + " " * (10 - len(loadNames[2])) + "Type: " + loadType[2] + " " * (12 - len(loadType[2])) + "Chapter: " + str(loadChp[2]))
            print("\n1. Slot 4 - Name: " + loadNames[3] + " " * (10 - len(loadNames[3])) + "Type: " + loadType[3] + " " * (12 - len(loadType[3])) + "Chapter: " + str(loadChp[3]))
            chosen = False
            while not chosen:
                try:
                    saveSlot = int(input("\nPlease choose an action: "))
                    if saveSlot > 4 or saveSlot <= 0:
                        saveSlot = int("stop")
                    chosen = True
                except Exception:
                    print("Please choose one of the available options")
            if loadNames[saveSlot - 1] != Player1.name and loadNames[saveSlot - 1] != "":
                    print("There is already a save in slot " + str(saveSlot) + ". Are you sure that you want to overwrite this slot?")
                    print("1. Yes")
                    print("2. No")
                    choice = 0
                    while choice == 0 or choice > 2:
                        try:
                            choice = int(input("\nPlease choose an action: "))
                            if choice == 1:
                                overwrite = True
                        except Exception:
                            print("Please choose one of the available options")
            else:
                overwrite = True
        dataList = list()
        dataList.append(Player1.name)
        dataList.append(Player1.type)
        dataList.append(Player1.health)
        dataList.append(Player1.armour)
        dataList.append(Player1.weaponDmg)
        dataList.append(Player1.crit)
        dataList.append(Player1.miss)
        dataList.append(Player1.numSlain)
        dataList.append(Player1.currentChp)
        match saveSlot:
            case 1:
                filePath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame1.txt"
            case 2:
                filePath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame2.txt"
            case 3:
                filePath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame3.txt"
            case 4:
                filePath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame4.txt"
        try:
            with open(filePath, "w") as file:
                json.dump(dataList, file)
                print("Game Saved Successfully\n")
                input("(Press ENTER to continue...)")
                os.system('cls')
        except Exception:
            print("Error saving game...\n")
            input("(Press ENTER to continue...)")
            os.system('cls')

    os.system("cls")
    print("Would you like to continue playing?\n")
    print("1. Yes\n2. No\n")
    choice = 0
    while choice == 0:
        try:
            choice = int(input("Please choose an action: "))
            if choice <= 0 or choice > 2:
                choice = int("stop")
        except Exception:
            print("Please choose one of the available options")
    match choice:
        case 1:
            os.system('cls')
            return 0
        case 2:
            os.system('cls')
            return 1
        
def loadGame(gameWindow, font1, Player1, clock):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    posX = 250
    posY = 200
    loadNames = [""] * 4
    loadChp = [""] * 4
    loadType = [""] * 4
    for x in range(1, 5):
        filePath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame" + str(x) + ".txt"
        try:
            with open(filePath, "r") as file:
                fileList = json.loads(file.read())
                z = 0
                for y in fileList:
                    if z == 0:
                        loadNames[x - 1] = y
                    elif z == 1:
                        loadType[x - 1] = y
                    elif z == 8:
                        loadChp[x -1] = y
                    z = z + 1
        except Exception:
            loadNames[x - 1] = ""
            loadType[x - 1] = ""
            loadChp[x -1] = ""

    for x in range(4):
        match loadType[x]:
            case 1:
                loadType[x] = "Barbarian"
            case 2:
                loadType[x] = "Knight"
            case 3:
                loadType[x] = "Assassin"
            case 4:
                loadType[x] = "Monk"
            case _:
                loadType[x] = ""
    
    gameWindow.fill(BLACK)
    textSurf = font1.render("Load Game", True, WHITE)
    gameWindow.blit(textSurf, (posX - 20, posY- 20))
    slot1 = font1.render("Slot 1 - Name: " + loadNames[0] + " " * (10 - len(loadNames[0])) + "Type: " + loadType[0] + " " * (12 - len(loadType[0])) + "Chapter: " + str(loadChp[0]), True, WHITE)
    slot2 = font1.render("Slot 2 - Name: " + loadNames[1] + " " * (10 - len(loadNames[1])) + "Type: " + loadType[1] + " " * (12 - len(loadType[1])) + "Chapter: " + str(loadChp[1]), True, WHITE)
    slot3 = font1.render("Slot 3 - Name: " + loadNames[2] + " " * (10 - len(loadNames[2])) + "Type: " + loadType[2] + " " * (12 - len(loadType[2])) + "Chapter: " + str(loadChp[2]), True, WHITE)
    slot4 = font1.render("Slot 4 - Name: " + loadNames[3] + " " * (10 - len(loadNames[3])) + "Type: " + loadType[3] + " " * (12 - len(loadType[3])) + "Chapter: " + str(loadChp[3]), True, WHITE)

    posY1 = posY + 50
    posY2 = posY + 100
    posY3 = posY + 150
    posY4 = posY + 200
    gameWindow.blit(slot1, (posX, posY1))
    gameWindow.blit(slot2, (posX, posY2))
    gameWindow.blit(slot3, (posX, posY3))
    gameWindow.blit(slot4, (posX, posY4))
    selected = 1
    pos2 = posY1 - 10
    pygame.draw.rect(gameWindow, WHITE, ((posX - 10), (posY1 - 10), 1200, 50), 1)
    pygame.display.flip()
    chosen = False
    while not chosen:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
                if event.key == pygame.K_DOWN:
                    if selected == 1:
                        if loadNames[1] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY2 - 10
                            selected = 2
                        elif loadNames[2] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY3 - 10
                            selected = 3
                        elif loadNames[3] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY4 - 10
                            selected = 4
                    elif selected == 2:
                        if loadNames[2] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY3 - 10
                            selected = 3
                        elif loadNames[3] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY4 - 10
                            selected = 4
                    elif selected == 3:
                        if loadNames[3] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY4 - 10
                            selected = 4
                if event.key == pygame.K_UP:
                    if selected == 4:
                        if loadNames[2] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY3 - 10
                            selected = 3
                        elif loadNames[1] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY2 - 10
                            selected = 2
                        elif loadNames[0] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY1 - 10
                            selected = 1
                    elif selected == 3:
                        if loadNames[1] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY2 - 10
                            selected = 2
                        elif loadNames[0] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY1 - 10
                            selected = 1
                    elif selected == 2:
                        if loadNames[0] != "":
                            pygame.draw.rect(gameWindow, BLACK, ((posX - 10), (pos2), 1200, 50), 1)
                            pos2 = posY1 - 10
                            selected = 1
                if event.key == pygame.K_RETURN:
                    chosen = True
                    filepath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame" + str(selected) + ".txt"
                    with open(filepath, 'r') as file:
                        fileList = json.loads(file.read())
                        y = 0
                        for x in fileList:
                            match y:
                                case 0:
                                    Player1.name = x
                                case 1:
                                    Player1.type = int(x)
                                case 2:
                                    Player1.health = int(x)
                                case 3:
                                    Player1.armour = int(x)
                                case 4:
                                    Player1.weaponDmg = int(x)
                                case 5:
                                    Player1.crit = int(x)
                                case 6:
                                    Player1.miss = int(x)
                                case 7:
                                    Player1.numSlain = int(x)
                                case 8:
                                    Player1.currentChp = int(x)
                            y = y + 1
                    return Player1
                pygame.draw.rect(gameWindow, WHITE, ((posX - 10), (pos2), 1200, 50), 1)
                pygame.display.flip()