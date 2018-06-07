import pygame as pg
import loader


class Obstaculo(pg.sprite.Sprite):
    def __init__(self, x, y, image, angle, width, height, radius, shape):
        super().__init__()
        self.x = x
        self.y = y
        self.image = loader.load(image)
        self.rect = self.image.get_rect()
        self.angle = angle
        self.width = width
        self.height = height
        self.radius = radius
        if shape == 'Rec':
            self.figure = (self.x, self.y, self.width, self.height)
        elif shape == 'Cir':
            self.figure = (self.x, self.y)
        elif shape == 'Line':
            self.figure = (
        
