# cambiar class player
# def init(self, x, y, angulo, score, img1, img2):
# def disparar(x, y, angulo, img_bala)
# comprobar main y Disparar tienen display variables igual

import pygame as pg

class Disparar(pg.sprite.Sprite):
    def __init__(self, x, y, angulo, img_bala, displayHeight, displayWidth):
        super().__init__()
        self.x = x
        self.y = y
        self.angulo = angulo
        self.bala = img_bala
        self.hitpoint = [x, y]
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth

    def bala(self):
        if self.rect.top > self.displayHeight:
            self.kill()
        elif self.rect.bottom < 0:
            self.kill()
        elif self.rect.left > self.displayWidth:
            self.kill()
        elif self.rect.right < 0:
            self.kill()
