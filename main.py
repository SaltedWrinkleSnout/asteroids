# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

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

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        pygame.display.flip()
        dt = fps_limit.tick(60)/1000



if __name__ == "__main__" :
    main()



