import circleshape
import constants 
import pygame
import random

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

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        angle1 = random.uniform(20, 50)
        random_angle = self.velocity.rotate(angle1)
        neg_random_angle = self.velocity.rotate(-angle1)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        first_half = Asteroid(self.position.x, self.position.y, new_radius)
        first_half.velocity = random_angle * 1.2

        second_half = Asteroid(self.position.x, self.position.y, new_radius)
        second_half.velocity = neg_random_angle * 1.2
