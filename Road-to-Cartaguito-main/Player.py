import pygame as pg
import Loader
import 

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, angle, score, img):
        super().__init__()
        self.x = x
        self.y = y
        self.angle = angle
        self.score = score
        self.self.maxSpeed = 5
        self.delta = 0.25
        self.img_player = img
        self.rect = self.img_player.image.get_rect()
        self.maxSpeed = 0
        self.delaS = 0
        self.rect.x = 600
        self.rect.y = 400

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
        Disparar.bala(self.x, self.y, self.angle)

    def scoreUp(self):
        self.score += 1

    def rotar(self):
        pg.transform.rotate(self.img_player, self.angle)
        



    
