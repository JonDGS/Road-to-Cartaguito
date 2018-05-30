import pygame as pg
import loader
import Disparar

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, angulo, score, img):
    super().__init__()
    self.x = x
    self.y = y
    self.angulo = angulo
    self.score = score
    self.maxSpeed = 5
    self.delta = 0.25
    self.img_player = img

    #def update()


    def moveUp(self):
        if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.xSpeed) >= maxspeed:
                    if self.xSpeed > 0:               
                        self.xSpeed -= deltaS         
                        self.ySpeed -= deltaS            #delta Velocidad 
                    else:                                #px/fps
                        self.xSpeed += deltaS            #      ^
                        self.ySpeed -= deltaS            #  8 - |          | 
                elif abs(self.ySpeed)>= maxspeed:        #  7 - |\         |
                    if self.ySpeed > 0:                  #  6 - | \        |
                        self.ySpeed -= deltaS            #  5 - |\ \       /
                    else: self.ySpeed = (maxspeed) * -1  #  4 - | \ \     /|
                else:                                    #  3 - |  \ \   / |
                    self.ySpeed -= deltaS                #  2 - |   \ \ /  |
                    if self.xSpeed > 0:                  #  1 - |    \ X   |
                        self.xSpeed -= deltaS            #  0 - |---- X-\--| 
                    elif self.xSpeed < 0:                # -1 - |    / \ \ |
                        self.xSpeed += deltaS            # -2 - |   /   \ \|
                    else:                                # -3 - |  /     \ |
                        self.xSpeed = 0                  # -4 - | /       \|
            else:                                        # -5 - |/.........\......>  tiempo*
                self.ySpeed -= deltaS


    def moveDown(self):
        if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.xSpeed) >= maxspeed:
                    if self.xSpeed > 0:                
                        self.xSpeed -= deltaS         
                        self.ySpeed += deltaS         
                    else:                             
                        self.xSpeed += deltaS         
                        self.ySpeed += deltaS         
                elif abs(self.ySpeed)>= maxspeed:        
                    if self.ySpeed < 0:
                        self.ySpeed += deltaS
                    else:
                        self.ySpeed = maxspeed
                else:                                       
                    self.ySpeed += deltaS                   
                    if self.xSpeed > 0:                     
                        self.xSpeed -= deltaS               
                    elif self.xSpeed < 0:                 
                        self.xSpeed += deltaS                
                    else:                                                
                        self.xSpeed = 0                             
            else:                                             
                self.ySpeed += deltaS


    def moveLeft(self):
        if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.ySpeed) >= maxspeed:
                    if self.ySpeed > 0:               
                        self.ySpeed -= deltaS         
                        self.xSpeed -= deltaS        
                    else:                           
                        self.ySpeed += deltaS         
                        self.xSpeed -= deltaS         
                elif abs(self.xSpeed)>= maxspeed:    
                    if self.xSpeed > 0:              
                        self.xSpeed -= deltaS      
                    else:
                        self.xSpeed = (maxspeed) * -1
                        self.ySpeed = 0
                else:                               
                    self.xSpeed -= deltaS            
                    if self.ySpeed > 0:             
                        self.ySpeed -= deltaS       
                    elif self.ySpeed < 0:            
                        self.ySpeed += deltaS       
                    else:                          
                        self.ySpeed = 0               
            else:                                     
                self.xSpeed -= deltaS


    def moveRight(self):
        if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.ySpeed) >= maxspeed:
                    if self.ySpeed > 0:                
                        self.ySpeed -= deltaS         
                        self.xSpeed += deltaS         
                    else:                             
                        self.ySpeed += deltaS         
                        self.xSpeed += deltaS         
                elif abs(self.xSpeed)>= maxspeed:        
                    if self.xSpeed < 0:
                        self.xSpeed += deltaS
                    else:
                        self.xSpeed = maxspeed
                        self.ySpeed = 0
                else:                                       
                    self.xSpeed += deltaS                   
                    if self.ySpeed > 0:                     
                        self.ySpeed -= deltaS               
                    elif self.ySpeed < 0:                 
                        self.ySpeed += deltaS                
                    else:                                                
                        self.ySpeed = 0                             
            else:                                             
                self.xSpeed += deltaS


    def disparar(self):
        Disparar.bala(x, y, angulo)


    def scoreUp(self):
        self.score += 1


    def rotar(self):
        pygame.transform.rotate(self.img_player, self.angle)
        



    
