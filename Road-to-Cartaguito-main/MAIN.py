import pygame as pg
import time
import loader
import enemy
#import Player

#Inicializar pygame
pg.init()
clock = pg.time.Clock()
S_width = 960
S_height = 720
screen = pg.display.set_mode((S_width, S_height))

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



test = True
while test:
    pg.
    img = pg.transform.scale(loader.load('Trump_Test_Image.png'), (S_width, S_height))
    screen.blit(img, (0, 0))
    clock.tick(60)
    pg.display.flip()







