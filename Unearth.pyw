from myGameMain import *
import pygame
from pygame.locals import *

pygame.init()
Game = main(True)

while Game.play:
    Game.play()

