import pygame as pg

class Loader(pg.sprite.Sprite):
    def __init__(self, image, angle):
        super().__init__()
        self.image = image
        self.angle = angle

    def rotate(self, image, angle):
        rot = pg.transform.rotate(image, angle)
        return rot

    def load(self, image):
        img = pg.image.load(image).convert()
        return img
