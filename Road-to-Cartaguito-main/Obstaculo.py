import pygame as pg
import loader


class Obstaculo(pg.sprite.Sprite):
    def __init__(self, x, y, image, angle):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
