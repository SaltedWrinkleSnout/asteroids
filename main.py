# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player
from constants import *
import asteroid
import asteroidfield

updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
shot_group = pygame.sprite.Group()

player.Player.containers = (updatable_group, drawable_group)
asteroid.Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
asteroidfield.AsteroidField.containers = (updatable_group)
player.Shot.containers = (shot_group, updatable_group, drawable_group)

def main():

    pygame.init()

    print("Starting Asteroids!")
    width = f"Screen width: {SCREEN_WIDTH}"
    height = f"Screen height: {SCREEN_HEIGHT}"
    print(width)
    print(height)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_limit = pygame.time.Clock()
    dt = 0 

    player1 = player.Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)) 

    Asteroids = asteroidfield.AsteroidField()

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        for drawable in drawable_group:
            drawable.draw(screen)

        updatable_group.update(dt)

        #check to see if the player has collided with an asteroid
        for bodies in asteroid_group:
            #print("checking for collisions")
            if player1.collide(bodies) :
                print("Game Over!")
                exit()


        pygame.display.flip()
        dt = fps_limit.tick(60)/1000



if __name__ == "__main__" :
    main()



