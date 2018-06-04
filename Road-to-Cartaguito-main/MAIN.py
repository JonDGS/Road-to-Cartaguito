import pygame as pg
import loader
import enemy
import Player
import disparar
#Para que se esta importando sys?
import sys
import Obstaculo
import Tools

# Inicializar pg
pg.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

fps = 30

displayWidth = 1200
displayHeight = 900
gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
clock = pg.time.Clock()

# Creacion de grupo de para todos los sprites del juego
all_sprites = pg.sprite.Group()

# Define cada objeto en su respectiva clase
player1 = Player.Player(0, 0, 0, 0)
player2 = Player.Player()
enemy = enemy.Enemy()
bullet = disparar.Disparar()
obstaculo = Obstaculo.Obstaculo()

# Anade los objetos al grupo total de Sprite
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(enemy)
all_sprites.add(bullet)
all_sprites.add(obstaculo)

# game loop
running = True

while running:

    clock.tick(fps)

    # check events y update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                pressed_left = True
            if event.key == pg.K_RIGHT:
                pressed_right = True
            if event.key == pg.K_UP:
                pressed_up = True
            if event.key == pg.K_DOWN:
                pressed_down = True
            if event.key == pg.K_SPACE:
                pressed_space = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                pressed_left = False
            if event.key == pg.K_RIGHT:
                pressed_right = False
            if event.key == pg.K_UP:
                pressed_up = False
            if event.key == pg.K_DOWN:
                pressed_down = False
            if event.key == pg.K_SPACE:
                pressed_space = False

        if pressed_up and pressed_right:
            Player.moveUp(), Player.moveRight()
        if pressed_up and pressed_left:
            Player.moveUp(), Player.moveLeft()
        if pressed_down and pressed_right:
            Player.moveDown(), Player.moveRight()
        if pressed_down and pressed_left:
            Player.moveDown(), Player.moveLeft()
        if pressed_up:
            Player.moveUp()
        if pressed_down:
            Player.moveDown()
        if pressed_left:
            Player.moveLeft()
        if pressed_right:
            Player.moveRight()
        if pressed_space:
            Player.disparar()

        # update todo
        all_sprites.update()

        # draw en la pantalla
        all_sprites.draw(gameDisplay)

        # Updates the display
        pg.display.flip()

pg.quit()
quit()
