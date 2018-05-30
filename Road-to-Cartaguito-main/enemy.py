import pygame
from loader import load

class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.posx = x
        self.posy = y
        self.image = load(image)

