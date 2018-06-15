import pygame
from pygame.locals import *
from math import *
import main
import car


music_menu = pygame.mixer.music.load('Stuff.wav')

# Define la superficie y font para el texto
def text_in_menu(text, color, font):
    textS = font.render(text, True, color)
    return textS, textS.get_rect()


# Define donde se mostrara el texto y con que color y tamaño
def mostrarTexto(text, x, y, size, color):
    TitleText = pygame.font.Font(ffx, size)
    TSurface, Trect = text_in_menu(text, color, TitleText)
    Trect.center = ((x, y))
    main.SCREEN.blit(TSurface, Trect)


# Loop del menu de scores
def menu1():
    m1 = True
    while m1:
        for event in pygame.event.get():
            if event.type == pressed:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == test_x:
                    m1 = False
                    #menus()
        main.SCREEN.blit(scorepng, (0, 0))
        mostrarTexto('Beta release v.0.3', (main.WIDTH * 0.10), (main.HEIGHT * 0.95), 15, light_green)
        main.FPS.tick(20)
        pygame.display.flip()

def menus():
    pygame.mixer.music.play(-1)
    Menus = True
    while Menus:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
            elif event.type == pressed:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == test_x:
                    menu1()
                elif event.key == pygame.K_1:
                    Menus = False
                    player2 = False
                    return ingreso(player2)
                elif event.key == pygame.K_2:
                    Menus = False
                    player2 = True
                    return ingreso(player2)
        main.SCREEN.fill(yellow)
        mostrarTexto("Road to Cartaguito", (main.WIDTH * 0.5), (main.HEIGHT * 1 / (72 / 20)), 58, black)
        mostrarTexto('Press 1 for solo or 2 for multiplayer', (main.WIDTH * 0.5), (main.HEIGHT * 0.7 // 1), 28, darkgreen)
        mostrarTexto('Press S to view scores', (main.WIDTH * 0.5), (main.HEIGHT * 0.75), 24, darkgreen)
        main.SCREEN.blit(Timage, (int(main.WIDTH * 0.20), int(main.HEIGHT * 0.35)))
        mostrarTexto('Beta release v.0.3', (main.WIDTH * 0.10), (main.HEIGHT * 0.95), 15, darkgreen)
        main.FPS.tick(20)
        pygame.display.flip()

def pause_menu(player2):
    pygame.mixer.music.pause()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                if event.key == pygame.K_m:
                    return menus()
                if event.key == pygame.K_r:
                    return menus()
                else:
                    mostrarTexto('Please press either enter escape to get back to game or m to go to the menus',
                                 (main.WIDTH * 0.50), (main.HEIGHT * 0.20), 30, red)
                    wait_x_secs(5)
        main.SCREEN.fill(white)
        main.SCREEN.blit(pause_background, (0, 0))
        mostrarTexto('Pause', (main.WIDTH * 0.50), (main.HEIGHT * 0.10), 50, black)
        mostrarTexto('Press m to got back to the menus', (main.WIDTH * 0.50), (main.HEIGHT * 0.20), 25, darkgreen)
        mostrarTexto("Press r to restart the game in it's current mode", (main.WIDTH * 0.50), (main.HEIGHT * 0.25), 25,
                     darkgreen)
        mostrarTexto("Press escape to get back into game", (main.WIDTH * 0.50), (main.HEIGHT * 0.30), 28, green)
        mostrarTexto('Beta release v.0.3', (main.WIDTH * 0.10), (main.HEIGHT * 0.95), 15, light_green)
        main.FPS.tick(20)
        pygame.display.update()