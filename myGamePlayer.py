# This is the supporting file
import os
import random
import time
from myGameEnemy import *
import pygame
from pygame.locals import *
from PIL import Image

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

    def getName(self, gamewindow, font1, clock):
        gamewindow.fill((0,0,0))

        loadImg = Image.open("c:/Users/nicho/Documents/My Creation/Art/Text Screens/background01.jpg")
        img = loadImg.resize((1600,900))
        img.save("c:/Users/nicho/Documents/My Creation/Art/Text Screens/background01.jpg")
        imgSurf = pygame.image.load("c:/Users/nicho/Documents/My Creation/Art/Text Screens/background01.jpg").convert()
        message = font1.render("What is your name?", True, (255,255,255))

        gamewindow.blit(imgSurf, (0,0))
        gamewindow.blit(message, message.get_rect(center = (800, 300)))
        pygame.draw.rect(gamewindow, (255,255,255), (575, 425, 450, 50), 1)
        pygame.display.flip()
        chosen = False
        text = ""
        while not chosen:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        chosen = True
                        break
                    elif event.key == pygame.K_RETURN:
                        if text != "":
                            chosen = True
                            self.name = text
                            break
                    elif event.key == K_BACKSPACE:
                        if len(text) > 0:
                            text = text[:-1]
                    else:
                        text += event.unicode
                playerName = font1.render(text, True, (255,255,255))
                gamewindow.blit(imgSurf, (0,0))
                gamewindow.blit(message, message.get_rect(center = (750, 300)))
                pygame.draw.rect(gamewindow, (255,255,255), (525, 420, 450, 50), 1)
                gamewindow.blit(playerName, playerName.get_rect(center = (740, 445)))
                pygame.display.flip()

    def getChar(self, gameWindow, font1, clock):
        imgSurf = pygame.image.load("c:/Users/nicho/Documents/My Creation/Art/Text Screens/background01.jpg").convert()
        message = font1.render("Choose your Character", True, (255,255,255))
        archetypes = ["Berserker", "Shaman", "Paladin", "Champion", "Ranger", "Assassin", "Monk", "Vagabond"]
        for x in range(8):
            archetypes[x] = font1.render(archetypes[x], True, (255,255,255))
        gameWindow.blit(imgSurf, (0,0))
        gameWindow.blit(message, message.get_rect(center = (750, 100)))

        pygame.draw.rect(gameWindow, (255, 255, 255), (200, 150, 250, 300), 4)
        pygame.draw.rect(gameWindow, (255, 255, 255), (500, 150, 250, 300), 4)
        pygame.draw.rect(gameWindow, (255, 255, 255), (800, 150, 250, 300), 4)
        pygame.draw.rect(gameWindow, (255, 255, 255), (1100, 150, 250, 300), 4)

        pygame.draw.rect(gameWindow, (255, 255, 255), (200, 500, 250, 300), 4)
        pygame.draw.rect(gameWindow, (255, 255, 255), (500, 500, 250, 300), 4)
        pygame.draw.rect(gameWindow, (255, 255, 255), (800, 500, 250, 300), 4)
        pygame.draw.rect(gameWindow, (255, 255, 255), (1100, 500, 250, 300), 4)
        
        gameWindow.blit(archetypes[0], archetypes[0].get_rect(center = (325, 475)))
        gameWindow.blit(archetypes[1], archetypes[1].get_rect(center = (625, 475)))
        gameWindow.blit(archetypes[2], archetypes[2].get_rect(center = (925, 475)))
        gameWindow.blit(archetypes[3], archetypes[3].get_rect(center = (1225, 475)))

        gameWindow.blit(archetypes[4], archetypes[4].get_rect(center = (325, 825)))
        gameWindow.blit(archetypes[5], archetypes[5].get_rect(center = (625, 825)))
        gameWindow.blit(archetypes[6], archetypes[6].get_rect(center = (925, 825)))
        gameWindow.blit(archetypes[7], archetypes[7].get_rect(center = (1225, 825)))
        

        pygame.display.flip()
        time.sleep(2)

    
    
    
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
