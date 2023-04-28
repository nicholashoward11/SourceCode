# This is my game... Enjoy
import os
import sys
import time
import json
from myGamePlayer import *
from myGameMenu import *
import pygame
from pygame.locals import *



class main():

    def __init__(self, playing):
        self.playing = playing

    def play(self, time0):
        Player1 = Player("", 0, 0, 0, 0, 0, 150, 0, 0)
        clock = pygame.time.Clock()
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
        pygame.display.flip()
        while not chosen:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        chosen = True
                        self.playing = False
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
                                "NEW GAME"
                                print(Player1.name, Player1.type, Player1.currentChp)
                            case 2:
                                "CONTINUE"
                                Player1 = loadGame(gameWindow, font1, Player1, clock)
                                if not Player1:
                                    break
                                else:
                                    gameWindow.fill(WHITE)
                                    namePlate = font1.render(Player1.name, True, BLACK)
                                    gameWindow.blit(namePlate, namePlate.get_rect(center = gameWindow.get_rect().center))
                                    pygame.display.flip()
                                    time.sleep(13)
                                    pygame.quit()
                                    sys.exit()
                            case 3:
                                "EXIT"
                                self.playing = False
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