import tkinter
from tkinter import *
import pygame
from math import *
import sys

displayWidth = 1280
displayHeight = 720

SCREEN = 0
clock = 0

running = False

#pygame.display.set_caption('Screen Wrapping')


track = 0

def run(boolean):
    running1 = boolean
    while not running1: 
        pygame.init()

def main():

    top.destroy()

    run(False)

    import prueba_ontrack





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
    player1n1=Text(modos,height=2,width=30)
    player1n1.pack()
    player1n1.place(x=500,y=230)
    p1_name_mode1 = player1n1.get("1.0",'end-1c')
    print(p1_name_mode1)

    player1n2=Text(modos,height=2,width=30)
    player1n2.pack()
    player1n2.place(x=500,y=430)
    p1_name_mode2 = player1n2.get("1.0",'end-1c')
    
    player2n2=Text(modos,height=2,width=30)
    player2n2.pack()
    player2n2.place(x=800,y=430)
    p2_name_mode2 = player2n2.get("1.0",'end-1c')
    modos.mainloop()

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
    confi.mainloop()

    
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

