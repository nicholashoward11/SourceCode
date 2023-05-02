import os
import keyboard
import json
import time
import pygame
from pygame.locals import *
from PIL import Image
# This is the story file


def chap1(gameWindow, Player1, clock):
    font = pygame.font.SysFont("Papyrus", 75)
    with open("c:/Users/nicho/Documents/My Creation/Story Files/Unearthed01.txt", 'r') as file:
        textFile = file.read()
        length = int((len(textFile) / 30) + 1)
        text = [""] * length
        x = 0
        for letter in textFile:
            if len(text[x]) >= 30 and letter == " ":
                x += 1
            text[x] += letter
    
    rectangles = [0] * (x + 1)
    for y in range(x + 1):
        rectangles[y] = font.render(text[y], True, (0,0,0))

    loadImg = Image.open("c:/Users/nicho/Documents/My Creation/Art/Text Screens/background02.jpg")
    img = loadImg.resize((1600,900))
    img.save("c:/Users/nicho/Documents/My Creation/Art/Text Screens/background02.jpg")
    imgSurf = pygame.image.load("c:/Users/nicho/Documents/My Creation/Art/Text Screens/background02.jpg").convert()
    
    low = 0
    difference = 450
    time0 = time.time()
    while time.time() < time0 + 36:
        clock.tick(60)
        gameWindow.blit(imgSurf, (0,0))
        low = difference
        for y in range(x + 1):
            gameWindow.blit(rectangles[y], rectangles[y].get_rect(center = (750, low)))
            low += 125
        pygame.display.flip()
        if difference == 450:
            time.sleep(2)
        difference -= 1


    


        

def chap2(Player1):
    match Player1.type:
        case 1:
            # Barbarian Subclass 1
            print("The first barbarian subclass")
        case 2:
            # Barbarian Subclass 2
            print("The second barbarian subclass")
        case 3:
            # Assassin Subclass 1
            print("The first assassin subclass")
        case 4:
            # Assassin Subclass 2
            print("The second assassin subclass")
        case 5:
            # Knight Subclass 1
            print("The first knight subclass")
        case 6:
            # Knight Subclass 2
            print("The second knight subclass")
        case 7:
            # Monk Subclass 1
            print("The first monk subclass")
        case 8:
            # Monk Subclass 2
            print("The second monk subclass")
    input("\n(Press ENTER to continue...)")
