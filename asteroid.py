import circleshape
import constants 
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y 
        self.radius = radius 

        super().__init__(self.x, self.y)

    def draw ():
        self.x, self.y self.radius, 2 
    
    def update():
        pass 
    