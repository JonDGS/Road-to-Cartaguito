import pygame as pg
import Tools
import loader
from math import *
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
track = pg.image.load('Track.png').convert()



def on_track(sprite):
    #Ver el color de pista bajo el carro y determina si esta en la pista o no.
    if sprite.x > 1 and sprite.x < displayWidth - 1 and sprite.y > 1 and sprite.y < displayHeight - 1:
        if track.get_at((int(sprite.x), int(sprite.y))).r == 163 or track.get_at((int(sprite.x), int(sprite.y))).r == 0 or track.get_at((int(sprite.x), int(sprite.y))).r == 255:
            return True
    return False

class Car(pg.sprite.Sprite):
    def __init__(self, start_pos = (73, 370), start_angle = 90, image = 'Car.png'):
        '''Initialises the Car object'''
        self.x     = start_pos[0]
        self.y     = start_pos[1]
        self.angle = start_angle
        self.speed = 0

        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (48, 48))

        self.rotcar   = pg.transform.rotate(self.image, self.angle)

    def move(self, forward_speed = 0.5, rearward_speed = 0.2):
        '''Moves the car when the arrow keys are pressed'''
        keys = pg.key.get_pressed()

        #determina que keys han sido pulsadas.
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.angle += self.speed
            
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.angle -= self.speed
            
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.speed += forward_speed
            
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.speed -= rearward_speed

        #define el angulo dentro de 360 grados
        self.angle %= 359

        #determina velocidad fuera o dentro del track
        if on_track(self): self.speed *= 0.95
        else: self.speed *= 0.75

        #cambia la posicion del carro tomando en cuenta el angulo.
        self.x += self.speed * cos(radians(self.angle))
        self.y -= self.speed * sin(radians(self.angle))

    def wrap(self):
        '''Wrap the car around the edges of the screen'''
        self.wrap_around = False

        if self.x <  0 :
            self.x += displayWidth
            self.wrap_around = True

        if self.x  + self.rotcar.get_width() > displayWidth:
            self.x -= displayWidth
            self.wrap_around = True

        if self.y  < 0:
            self.y += displayHeight
            self.wrap_around = True

        if self.y + self.rotcar.get_height() > displayHeight:
            self.y -= displayHeight
            self.wrap_around = True

        if self.wrap_around:
            SCREEN.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))

        self.x %= displayWidth
        self.y %= displayHeight

    def render(self):
        '''Renders the car on the screen'''
        self.rotcar   = pg.transform.rotate(self.image, self.angle)

        gameDisplay.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))

#control de loops

main_loop = False
def main_loop():
    car   = Car()
    while main_loop:
        #Blit the track to the background
        gameDisplay.blit(track, (0, 0))

        #Test if the game has been quit
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

        car.move()
        car.wrap()
        car.render()

        pg.display.update()
        clock.tick(fps)
main_loop()

mode_selection_loop = False
def mode_selection():
    #pg.event.wait()
    rect1 = pg.Rect(displayWidth * 0.1, displayHeight * 0.8, 200, 100)
    rect2 = pg.Rect(displayWidth * (952/1280), displayHeight * 0.8, 200, 100)
    active1 = False
    active2 = False
    gameDisplay.fill(blue)
    pg.draw.rect(gameDisplay, red, rect1)
    pg.draw.rect(gameDisplay, red, rect2)
    clock.tick(60)
    pg.display.flip()
    
    while mode_selection_loop == True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    Menu = False
                    pg.QUIT()
                    quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    active1 = True
                    print('Llego a 1 jugador')
                #if rect1.collidepoint(event.pos):
                if rect2.collidepoint(event.pos):
                    active2 = True
                    print('Llego a 2 jugadores')
            elif active1:
                main_loop()
            elif active2:
                main_loop()
        
mode_selection()

def menu_principal():
    #pg.event.wait()
    rect1 = pg.Rect(displayWidth * 0.1, displayHeight * 0.8, 200, 100)
    rect2 = pg.Rect(displayWidth * (952/1280), displayHeight * 0.8, 200, 100)
    menu_principal = True 
    active1 = False
    active2 = False
    while menu_principal:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    menu_principal = False
                    pg.QUIT()
                    quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    active1 = True
                    mode_selection_loop = True
                    menu_principal = False
                    print('Llego a mode selection')
                #if rect1.collidepoint(event.pos):
                if rect2.collidepoint(event.pos):
                    active2 = True
                    print('Llego a scores')
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
