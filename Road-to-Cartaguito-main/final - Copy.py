import pygame as pg
import os

# Inicializar pg
pg.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

fps = 30

displayWidth = 1280
displayHeight = 720
gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
clock = pg.time.Clock()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img_folder")
mapa = pg.image.load(os.path.join(img_folder, "track2,0.jpg")).convert()
player1_img = pg.image.load(os.path.join(img_folder, "testcar1.png")).convert()
player2_img = pg.image.load(os.path.join(img_folder, "testcar2.png")).convert()



#clase player

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, angle, score, image):
        super().__init__()
        self.x = x
        self.y = y
        self.angle = angle
        self.score = score
        self.maxSpeed = 5
        self.delta = 0.25
        self.img = image
        self.rect = self.img.get_rect()
        self.maxSpeed = 0
        self.delaS = 0
        self.rect.x = 600
        self.rect.y = 400
        self.start = [self.x, self.y, self.angle, self.score, self.img]

    def moveUp(self):
        if abs(self.xSpeed) + abs(self.ySpeed) >= self.maxspeed:
                if abs(self.xSpeed) >= self.maxspeed:
                    if self.xSpeed > 0:               
                        self.xSpeed -= self.deltaS
                        self.ySpeed -= self.deltaS            #delta Velocidad
                    else:                                #px/fps
                        self.xSpeed += self.deltaS            #      ^
                        self.ySpeed -= self.deltaS            #  8 - |          |
                elif abs(self.ySpeed)>= self.maxspeed:        #  7 - |\         |
                    if self.ySpeed > 0:                  #  6 - | \        |
                        self.ySpeed -= self.deltaS            #  5 - |\ \       /
                    else: self.ySpeed = (self.maxspeed) * -1  #  4 - | \ \     /|
                else:                                    #  3 - |  \ \   / |
                    self.ySpeed -= self.deltaS                #  2 - |   \ \ /  |
                    if self.xSpeed > 0:                  #  1 - |    \ X   |
                        self.xSpeed -= self.deltaS            #  0 - |---- X-\--|
                    elif self.xSpeed < 0:                # -1 - |    / \ \ |
                        self.xSpeed += self.deltaS            # -2 - |   /   \ \|
                    else:                                # -3 - |  /     \ |
                        self.xSpeed = 0                  # -4 - | /       \|
        else:                                        # -5 - |/.........\......>  tiempo*
            self.ySpeed -= self.deltaS

    def moveDown(self):
        if abs(self.xSpeed) + abs(self.ySpeed) >= self.maxspeed:
                if abs(self.xSpeed) >= self.maxspeed:
                    if self.xSpeed > 0:                
                        self.xSpeed -= self.deltaS
                        self.ySpeed += self.deltaS
                    else:                             
                        self.xSpeed += self.deltaS
                        self.ySpeed += self.deltaS
                elif abs(self.ySpeed)>= self.maxspeed:
                    if self.ySpeed < 0:
                        self.ySpeed += self.deltaS
                    else:
                        self.ySpeed = self.maxspeed
                else:                                       
                    self.ySpeed += self.deltaS
                    if self.xSpeed > 0:                     
                        self.xSpeed -= self.deltaS
                    elif self.xSpeed < 0:                 
                        self.xSpeed += self.deltaS
                    else:                                                
                        self.xSpeed = 0                             
        else:                                             
            self.ySpeed += self.deltaS

    def moveLeft(self):
        if abs(self.xSpeed) + abs(self.ySpeed) >= self.maxspeed:
                if abs(self.ySpeed) >= self.maxspeed:
                    if self.ySpeed > 0:               
                        self.ySpeed -= self.deltaS
                        self.xSpeed -= self.deltaS
                    else:                           
                        self.ySpeed += self.deltaS
                        self.xSpeed -= self.deltaS
                elif abs(self.xSpeed)>= self.maxspeed:
                    if self.xSpeed > 0:              
                        self.xSpeed -= self.deltaS
                    else:
                        self.xSpeed = (self.maxspeed) * -1
                        self.ySpeed = 0
                else:                               
                    self.xSpeed -= self.deltaS
                    if self.ySpeed > 0:             
                        self.ySpeed -= self.deltaS
                    elif self.ySpeed < 0:            
                        self.ySpeed += self.deltaS
                    else:                          
                        self.ySpeed = 0               
        else:
            self.xSpeed -= self.deltaS

    def moveRight(self):
        if abs(self.xSpeed) + abs(self.ySpeed) >= self.maxspeed:
                if abs(self.ySpeed) >= self.maxspeed:
                    if self.ySpeed > 0:                
                        self.ySpeed -= self.deltaS
                        self.xSpeed += self.deltaS
                    else:                             
                        self.ySpeed += self.deltaS
                        self.xSpeed += self.deltaS
                elif abs(self.xSpeed)>= self.maxspeed:
                    if self.xSpeed < 0:
                        self.xSpeed += self.deltaS
                    else:
                        self.xSpeed = self.maxspeed
                        self.ySpeed = 0
                else:                                       
                    self.xSpeed += self.deltaS
                    if self.ySpeed > 0:                     
                        self.ySpeed -= self.deltaS
                    elif self.ySpeed < 0:                 
                        self.ySpeed += self.deltaS
                    else:                                                
                        self.ySpeed = 0                             
        else:                                             
            self.xSpeed += self.deltaS

    def disparar(self):
        bullet.bala(self.x, self.y, self.angle)

    def scoreUp(self):
        self.score += 1

    def rotar(self):
        self.image = loader.rotate(self.image, self.angle)



# Creacion de grupo de para todos los sprites del juego
all_sprites = pg.sprite.Group()

# Define cada objeto en su respectiva clase

                       #x,y, angle, score, img
player1 = Player(20, 20, 0, 0, player1_img)
#player2 = Player.Player()
#enemy = enemy.Enemy()
#bullet = bullet.Disparar()
#obstaculo = Obstaculo.Obstaculo()

# Anade los objetos al grupo total de Sprite
all_sprites.add(player1)
#all_sprites.add(player2)
#all_sprites.add(enemy)
#all_sprites.add(bullet)
#all_sprites.add(obstaculo)

# game loop
running = True

while running:

    clock.tick(fps)

    # check events y update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
        pressed_up = False
        pressed_down = False
        pressed_left = False
        pressed_right = False
        pressed_space = False

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

        # update all
        all_sprites.update()

        # draw en la pantalla
        gameDisplay.blit(mapa, (0,0))
##        all_sprites.draw(gameDisplay)

        # flips the display
        pg.display.flip()

pg.quit()
quit()
