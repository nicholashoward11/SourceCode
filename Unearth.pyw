from myGameMain import *
import pygame
from pygame.locals import *

pygame.init()
Game = main(True)
time0 = time.time()

while Game.playing:
    Game.play(time0)

pygame.quit()
sys.exit