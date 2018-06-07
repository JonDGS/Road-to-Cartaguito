import pygame as pg
import Tools
import loader
#import MAIN

# Inicializar pg
pg.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

fps = 30

displayWidth = 1280
displayHeight = 720
gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
clock = pg.time.Clock()

def menu_principal():
    #pg.event.wait()
    rect1 = pg.Rect(displayWidth * 0.1, displayHeight * 0.8, 200, 100)
    rect2 = pg.Rect(displayWidth * (952/1280), displayHeight * 0.8, 200, 100)
    active1 = False
    active2 = False
    Menu = True
    while Menu:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    Menu = False
                    pg.QUIT()
                    quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    active1 = True
                    print('Llego aqui')
                if rect1.collidepoint(event.pos):
                    active2 = True
                    print('Llego aqui')
            elif active1:
                mode_selection()
            elif active2:
                scores()
        gameDisplay.fill(yellow)
        pg.draw.rect(gameDisplay, red, rect1)
        pg.draw.rect(gameDisplay, red, rect2)
        clock.tick(60)
        pg.display.flip()
menu_principal()
                        
                    
                    
        
        
