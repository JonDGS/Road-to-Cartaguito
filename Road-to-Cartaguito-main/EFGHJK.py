import tkinter
from tkinter import *
import pygame
from math import *
import sys

displayWidth = 1280
displayHeight = 720

def run(boolean):
running = True
while not running: 
    pygame.init()
    SCREEN = pygame.display.set_mode((displayWidth,displayHeight))
    clock = pygame.time.Clock()

    pygame.display.set_caption('Screen Wrapping')


    track = pygame.image.load('Track.png').convert()

def main():
        car1   = Car()

        while running == True:
            #Blit the track to the background
            SCREEN.blit(track, (0, 0))

            #Test if the game has been quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            car1.move()
            car1.wrap()
            car1.render()

            pygame.display.update()
            clock.tick(30)

def on_track(sprite):
    #Ver el color de pista bajo el carro y determina si esta en la pista o no.
    if sprite.x > 1 and sprite.x < displayWidth - 1 and sprite.y > 1 and sprite.y < displayHeight - 1:
        if track.get_at((int(sprite.x), int(sprite.y))).r == 163 or track.get_at((int(sprite.x), int(sprite.y))).r == 0 or track.get_at((int(sprite.x), int(sprite.y))).r == 255:
            return True
        return False

    class Car(object):
        def __init__(self, start_pos = (73, 370), start_angle = 90, image = 'Car.png'):
            '''Initialises the Car object'''
            self.x     = start_pos[0]
            self.y     = start_pos[1]
            self.angle = start_angle
            self.speed = 0

            self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (48, 48))

            self.rotcar   = pygame.transform.rotate(self.image, self.angle)

        def move(self, forward_speed = 1, rearward_speed = 0.2):
            '''Moves the car when the arrow keys are pressed'''
            keys = pygame.key.get_pressed()

            #Move the car depending on which keys have been pressed
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.angle += self.speed
                
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.angle -= self.speed
                
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.speed += forward_speed
                
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.speed -= rearward_speed

            #Keep the angle between 0 and 359 degrees
            self.angle %= 359

            #Apply friction
            if on_track(self): self.speed *= 0.95
            else: self.speed *= 0.75

            #Change the position of the car
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
            self.rotcar   = pygame.transform.rotate(self.image, self.angle)

            SCREEN.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))



def seleccion_de_modos():
    top.withdraw()
    modos=Toplevel()
    modos.title("Seleccion de juego")
    modos.minsize(displayWidth,displayHeight)
    modos.resizable(width=NO,height=NO)
    cmodos=Canvas(modos,width=displayWidth,height=displayHeight,bg="blue")
    cmodos.place(x=0,y=0)
    but6=Button(modos, text = "1 jugador", command = main, bg = "green", fg = "white", width = 32, height = 4)
    but6.place(x=200,y=200)
    but7=Button(modos, text = "2 jugadores", command = main, bg = "green", fg = "white", width = 32, height = 4)
    but7.place(x=200,y=400)
    but8=Button(modos, text = "otras posibles pokemadres", command = main, bg = "green", fg = "white", width = 32, height = 4)
    but8.place(x=200,y=600)

def configuraciones():
    top.withdraw()
    confi=Toplevel()
    confi.title("Configuraciones")
    confi.minsize(displayWidth,displayHeight)
    confi.resizable(width=NO,height=NO)
    cconfi=Canvas(confi,width=displayWidth,height=displayHeight,bg="blue")
    cconfi.place(x=0,y=0)
    but3=Button(confi, text = "configuracion 1", command = top, bg = "green", fg = "black", width = 32, height = 4)
    but3.place(x=200,y=200)
    but4=Button(confi, text = "configuracion 2", command = top, bg = "green", fg = "black", width = 32, height = 4)
    but4.place(x=200,y=400)
    but5=Button(confi, text = "configuracion n", command = top, bg = "green", fg = "black", width = 32, height = 4)
    but5.place(x=200,y=600)

    
#define ventana llamada "top"
top=Tk()
#da titulo a la ventana
top.title("Menu Principal")
#da tamaño de ventana
top.minsize(displayWidth,displayHeight)
#obligatorio \ para hacer resize
top.resizable(width=NO,height=NO)
#crea un surface para hacer botones
ctop=Canvas(top,width=displayWidth,height=displayHeight,bg="yellow")
#dice donde crear el surface
ctop.place(x=0,y=0)
#crea un boton en el surface "top"
boton1 = Button(top, text = "Seleccion de modos", command = seleccion_de_modos, bg = "blue", fg = "white", width = 32, height = 4)
boton2 =Button(top, text = "Configuraciones", command = configuraciones, bg = "blue", fg = "white", width = 32, height = 4)
#da ubicacion de boton
boton1.place(x=displayWidth * 0.1,y=displayHeight * 0.8)
boton2.place(x=displayWidth * (952/1280), y=displayHeight * 0.8)
#???
top.mainloop()

main()

