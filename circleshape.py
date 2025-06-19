import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, other):
        #if distance between self and other <= r1+r2 then return True
        distance_between = self.position.distance_to(other.position)
        #print(f"Distance: {distance_between}, Sum of radii: {self.radius + other.radius}")
        return(distance_between <= self.radius + other.radius)