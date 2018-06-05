#cambiar class player
# def init(self, x, y, angulo, score, img1, img2):
# def disparar(x, y, angulo, img_bala)
# comprobar main y Disparar tienen display variables igual

import pygame as pg
import loader
import MAIN

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, angle, image):
        super().__init__()
        self.x = x
        self.y = y
        self.angle = angle
        self.image = loader.load(image)
        self.rect = self.image.get_rect()

    def disparar(self):
        if self.x > 0:
            x

    def disappear(self):
        if self.rect.top > MAIN.S_height:
            self.kill()
        elif self.rect.bottom < 0:
            self.kill()
        elif self.rect.left > MAIN.S_width:
            self.kill()
        elif self.rect.right < 0:
            self.kill()
    #def crash(self):

