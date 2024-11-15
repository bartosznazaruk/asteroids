# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (all_shots, updatable, drawable)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for thing in updatable:
            thing.update(dt)

        for thing in all_asteroids:
            if thing.collision_check(player):
                print("Game over!")
                sys.exit()

            for bullet in all_shots:
                if thing.collision_check(bullet):
                    thing.split()
                    bullet.kill()

        for thing in drawable:
            thing.draw(screen)   
       
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()