import pygame as pg
import loader


class Obstaculo(pg.sprite.Sprite):
    def __init__(self, x, y, image, angulo):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.angulo = angulo

    def rotar(self):
        pg.transform.rotate(self.image, self.angle)
