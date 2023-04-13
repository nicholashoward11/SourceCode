# This is my game... Enjoy
import os
import time
import json
from myGamePlayer import *
import pygame
from pygame.locals import *


class main():

    def __init__(self, playing):
        self.playing = True

    def loadGame(gameWindow, clock, font1, Player1):
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
        while inLoading:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inMenu = True
                        inLoading = False
                        break
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


    def play():
        Player1 = Player("", 0, 0, 0, 0, 0, 150, 0, 0)
        clock = pygame.time.clock()
        time0 = time.time()
        font1 = pygame.font.SysFont("Consolas", 35)
        font2 = pygame.font.SysFont("Consolas", 20)
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        gameWindow = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        text = "UNEARTH"
        while time.time() < time0 + 5:
            clock.tick(30)
            gameWindow.fill(BLACK)
            textSurf = font1.render(text, True, WHITE)
            gameWindow.blit(textSurf, textSurf.get_rect(center = gameWindow.get_rect().center))
            if time.time() > time0 + 2:
                text = "by Nicholas"
            if time.time() > time0 + 4:
                text = "Welcome"
            pygame.display.flip()
        gameWindow.fill((0,0,0))
        textSurf = font1.render("UNEARTH", True, WHITE)
        option1 = font2.render("New Game", True, WHITE)
        option2Exists = False
        count = 0
        for x in range(1, 5, 1):
            filePath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame" + str(x) + ".txt"
            try:
                with open(filePath, "r") as file:
                    fileList = json.loads(file.read())
                    z = 0
                    for y in fileList:
                        if z == 0:
                            if y != "":
                                count += 1
                        z += 1
            except Exception:
                break
        if count > 0:
            option2Exists = True
            option2 = font2.render("Continue", True, WHITE)
        option3 = font2.render("Quit", True, WHITE)
        posX = 250
        posY = 200
        posY1 = 0
        posY2 = 0
        posY3 = 0
        gameWindow.blit(textSurf, (posX,posY))
        posY1 = 50 + posY
        gameWindow.blit(option1, (posX,posY1))
        posY2 = 30 + posY1
        if option2Exists:
            gameWindow.blit(option2, (posX,posY2))
            posY3 = 30 + posY2
        else:
            posY3 = posY2
        gameWindow.blit(option3, (posX,posY3))
        rect1 = (posX - 5, posY1 - 5, 98, 30)
        if option2Exists:
            rect2 = (posX - 5, posY2 - 5, 98, 30)
        rect3 = (posX - 5, posY3 - 5, 54, 30)
        pos1 = rect1
        pygame.draw.rect(gameWindow, WHITE, pos1, 1)
        chosen = False
        selected = 1
        







        
    while inMenu:
        gameWindow.fill((0,0,0))
        textSurf = font1.render("UNEARTH", True, WHITE)
        option1 = font2.render("New Game", True, WHITE)
        option2Exists = False
        count = 0
        for x in range(1, 5, 1):
            filePath = "c:/Users/nicho/Documents/My Creation/Game Saves/SaveGame" + str(x) + ".txt"
            try:
                with open(filePath, "r") as file:
                    fileList = json.loads(file.read())
                    z = 0
                    for y in fileList:
                        if z == 0:
                            if y != "":
                                count += 1
                        z += 1
            except Exception:
                break
        if count > 0:
            option2Exists = True
            option2 = font2.render("Continue", True, WHITE)
        option3 = font2.render("Quit", True, WHITE)
        posX = 250
        posY = 200
        posY1 = 0
        posY2 = 0
        posY3 = 0
        gameWindow.blit(textSurf, (posX,posY))
        posY1 = 50 + posY
        gameWindow.blit(option1, (posX,posY1))
        posY2 = 30 + posY1
        if option2Exists:
            gameWindow.blit(option2, (posX,posY2))
            posY3 = 30 + posY2
        else:
            posY3 = posY2
        gameWindow.blit(option3, (posX,posY3))
        rect1 = (posX - 5, posY1 - 5, 98, 30)
        if option2Exists:
            rect2 = (posX - 5, posY2 - 5, 98, 30)
        rect3 = (posX - 5, posY3 - 5, 54, 30)
        pos1 = rect1
        pygame.draw.rect(gameWindow, WHITE, pos1, 1)
        chosen = False
        selected = 1
        pygame.display.flip()
        while not chosen:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inMenu = False
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inMenu = False
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if selected == 1 and option2Exists:
                            pygame.draw.rect(gameWindow, BLACK, pos1, 1)
                            pos1 = rect2
                            selected = 2
                        elif selected == 1 or selected == 2:
                            pygame.draw.rect(gameWindow, BLACK, pos1, 1)
                            pos1 = rect3
                            selected = 3
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if selected == 3 and option2Exists:
                            pygame.draw.rect(gameWindow, BLACK, pos1, 1)
                            pos1 = rect2
                            selected = 2
                        elif selected == 3 or selected == 2:
                            pygame.draw.rect(gameWindow, BLACK, pos1, 1)
                            pos1 = rect1
                            selected = 1
                    if event.key == pygame.K_RETURN :
                        chosen = True
                        match selected:
                            case 1:
                                Player1 = Player("", 0, 0, 0, 0, 0, 150, 0, 0)
                                inMenu = False
                            case 2:
                                inMenu = False
                                inLoading = True
                                

                            case 3:
                                pygame.quit()
                    pygame.draw.rect(gameWindow, WHITE, pos1, 1)
                    pygame.display.flip()
                
        

    """ Player1 = Player("", 0, 0, 0, 0, 0, 150, 0, 0)
    quiting = mainMenu(Player1)
    if Player1.currentChp == 0 and quiting != 1:
        Player1.getName()
        Player1.getChar()
        Player1.currentChp = 1
        quiting = saveGame(Player1)

    if Player1.currentChp == 1 and quiting != 1:
        chap1(Player1)
        goblin1 = enemy(60, 5, 10, 15, 15, False)
        won = combat1(Player1, goblin1)
        if won == True:
            Player1.currentChp = 2
            quiting = saveGame(Player1)
        os.system('cls')

    if Player1.currentChp == 2 and quiting != 1: 
        chap2(Player1)
        level1 = enemy(60, 5, 10, 15, 15, False)
        level2 = enemy(60, 5, 10, 15, 15, False)
        won = combat2(Player1, level1, level2)
        if won:
            Player1.currentChp = 3
            quiting = saveGame(Player1)

    if Player1.currentChp == 3 and quiting != 1:
        os.system('cls')
        print("This is the end of the demo... Thanks for playing\n\n")
        input("(Press ENTER to continue...)")
 """