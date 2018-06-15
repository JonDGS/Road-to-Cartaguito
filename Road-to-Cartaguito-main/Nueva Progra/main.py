import sys, pygame
from pygame.locals import *
from math import *
import car


pygame.init()

WIDTH  = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS    = pygame.time.Clock()

pygame.display.set_caption('road to cartaguito')

track = pygame.image.load('track.png').convert()


#Funcion que sabe si el vehiculo esta en la pista o fuera de ella
def on_track(sprite, con1, con2, con3):
    #Condiciones para cada nivel
    if con1 and not con2 and not con3:
        if sprite.x > 1 and sprite.x < WIDTH - 1 and sprite.y > 1 and sprite.y < HEIGHT - 1:
            if track.get_at((int(sprite.x), int(sprite.y))).r == 163 or track.get_at((int(sprite.x), int(sprite.y))).r == 0 or track.get_at((int(sprite.x), int(sprite.y))).r == 255:
                return True
        return False
    if con1 and con2 and not con3:
        if sprite.x > 1 and sprite.x < WIDTH - 1 and sprite.y > 1 and sprite.y < HEIGHT - 1:
            if track.get_at((int(sprite.x), int(sprite.y))).r == 163 or track.get_at((int(sprite.x), int(sprite.y))).r == 0 or track.get_at((int(sprite.x), int(sprite.y))).r == 255:
                return True
        return False
    if con1 and not con2 and con3:
        if sprite.x > 1 and sprite.x < WIDTH - 1 and sprite.y > 1 and sprite.y < HEIGHT - 1:
            if track.get_at((int(sprite.x), int(sprite.y))).r == 163 or track.get_at((int(sprite.x), int(sprite.y))).r == 0 or track.get_at((int(sprite.x), int(sprite.y))).r == 255:
                return True
        return False
#Loop del nivel 1
def level_one(car1, car2):
    car1.first_level = True
    car2.first_level = True
    running = True
    while True:
        #Blit the track to the background
        SCREEN.blit(track, (0, 0))
        #print(car1.self)

        #Test if the game has been quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        car1.move()
        car1.wrap()
        car1.render()
        car2.move()
        car2.wrap()
        car2.render()

        pygame.display.update()
        FPS.tick(30)

#Loop princioal del juego
def main():
    car1   = car.Car((53, 370), 90, 'Car1.png', [K_LEFT, K_RIGHT, K_UP, K_DOWN], 'Test1', 0, 0, 0)
    car2   = car.Car((83, 370), 90, 'Car.png', [K_a, K_d, K_w, K_s], 'Test2', 0, 0, 0)

    level_one(car1, car2)

if __name__ == '__main__': main()
