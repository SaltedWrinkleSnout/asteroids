import circleshape
import constants 
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y 
        self.radius = radius 

        super().__init__(self.x, self.y,self.radius)

    def draw (self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 
    
    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)