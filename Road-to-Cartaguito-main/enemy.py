import pygame as pg


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.angle = 0
        self.image = loader.load(image)
        self.start = [x, y, self.angle, loader.rotate(self.image, self.angle)]
        self.speed = 0.25
    #Methods
    def start(self):
        self.x = self.start[0]
        self.y = self.start[1]
        self.angle = self.start[2]
        self.image = self.start[3]
    def ANI1(self):
        pass
    def ANI2(self):
        pass
    def ANI3(self):
        pass

