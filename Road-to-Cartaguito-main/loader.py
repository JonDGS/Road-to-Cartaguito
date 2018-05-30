import pygame as pg

def rotate(image, angle):
    rot = pg.transform.rotate(image, angle)
    return rot

def load(image):
    img = pg.image.load(image)
    return img
