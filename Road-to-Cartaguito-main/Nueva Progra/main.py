import sys, pygame
from pygame.locals import *
from math import *
import car
import SavesManager


pygame.init()

WIDTH  = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS    = pygame.time.Clock()

pygame.display.set_caption('road to cartaguito')

track = pygame.image.load('track.png').convert()
track2 = pygame.image.load('track2.png').convert()
track3 = pygame.image.load('track3.png').convert()


#Funcion que sabe si el vehiculo esta en la pista o fuera de ella
def on_track(sprite):
    #Condiciones para cada nivel
    if sprite.x > 1 and sprite.x < WIDTH - 1 and sprite.y > 1 and sprite.y < HEIGHT - 1:
        if track.get_at((int(sprite.x), int(sprite.y))).r == 163 or track.get_at((int(sprite.x), int(sprite.y))).r == 0 or track.get_at((int(sprite.x), int(sprite.y))).r == 255:
            print('Llego')
            return True
    return False
#Loop del nivel 1
def level_three(car1, car2):
    car1.x, car1.y = (334, 524)
    car2.x, car2.y = (334, 484)
    car1.angle = 180
    car2.angle = 180
    running = True
    while running:
        #Blit the track to the background
        SCREEN.blit(track3, (0, 0))
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
    SavesManager.leaderboard(car1.username, car1.total, car1.laps, car1.hits)
#Loop del nivel 1
def level_two(car1, car2):
    car1.x, car1.y = (370, 47)
    car2.x, car2.y = (370, 77)
    car1.angle = 0
    car2.angle = 0
    running = True  
    while running:
        #Blit the track to the background
        SCREEN.blit(track2, (0, 0))
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
    level_three(car1, car2)
#Loop del nivel 1
def level_one(car1, car2):
    car1.x, car1.y = (53, 370)
    car2.x, car2.y = (83, 370)
    car1.angle = 90
    car2.angle = 90
    running = True
    while running:
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
        mouse = pygame.mouse.get_pos()
        car1.move()
        car1.wrap()
        car1.render()
        car2.move()
        car2.wrap()
        car2.render()

        pygame.display.update()
        FPS.tick(30)
    level_two(car1, car2)

#Loop princioal del juego
def main():
    car1   = car.Car((0, 0), 0, 'Car1.png', [K_LEFT, K_RIGHT, K_UP, K_DOWN], 'Test1', 0, 0, 0)
    car2   = car.Car((0, 0), 0, 'Car.png', [K_a, K_d, K_w, K_s], 'Test2', 0, 0, 0)

    level_two(car1, car2)

if __name__ == '__main__': main()
