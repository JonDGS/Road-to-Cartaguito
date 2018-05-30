import pygame as pg
#Define la superficie y font para el texto
def text_rendering(text, color, font):
    textS = font.render(text, True, color)
    return textS, textS.get_rect()


# Define donde se mostrara el texto y con que color y tamaño
def mostrarTexto(text, x, y, size, color):
    TitleText = pg.font.Font(ffx, size)
    TSurface, Trect = text_rendering(text, color, TitleText)
    Trect.center = ((x, y))
    screen.blit(TSurface, Trect)