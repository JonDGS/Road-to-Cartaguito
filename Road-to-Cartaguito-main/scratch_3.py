import pygame
import loader

class player(pygame.sprite.Sprite):
    def __init__(self,username, x, y, image):
        super().__init__()
        self.username = username
        self.posx = x
        self.posy = y
        self.speed = 0
        self.ms2 = 1.5
        self.minusms2 = 2
        self.image = loader.load(image)
        self.angle = 0
        self.maxspeed = 6
        self.minspeed = 0
        self.U = False
        self.D = False
        self.R = False
        self.L = False
    def move_up(self):
        self.U = True
        self.angle = 0
        self.posy += -self.speed
    def move_down(self):
        self.D = True
        self.angle = 180
        self.posy += self.speed
    def move_right(self):
        self.R = True
        self.angle = 270
        self.posx += self.speed
    def move_left(self):
        self.L = True
        self.angle = 180
        self.posx += -self.speed
    def release_up(self):
        self.U = False
    def release_down(self):
        self.D = False
    def release_right(self):
        self.R = False
    def release_left(self):
        self.L = False
    def acceleration(self):
        if self.speed < self.maxspeed:
            self.speed += self.ms2
        else:
            pass
    def deccelerate(self):
        if self.speed > self.minspeed:
            self.speed -= self.minusms2
        else:
            pass



