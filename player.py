import circleshape
import constants 
import pygame


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y 

        super().__init__(self.x, self.y, constants.PLAYER_RADIUS)

        self.rotation = 0 

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (constants.PLAYER_TURN_SPEED*dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        angle = pygame.Vector2(0,1).rotate(self.rotation)
        Shot(self.position.x, self.position.y, angle)
        
        

class Shot(circleshape.CircleShape):
        def __init__(self, x, y, angle):
            self.radius = constants.SHOT_RADIUS 
            self.position = pygame.Vector2(x,y)
            self.angle = angle

            super().__init__(self.position.x, self.position.y, self.radius)

            self.velocity.x = self.angle.x * constants.PLAYER_SHOOT_SPEED
            self.velocity.y = self.angle.y * constants.PLAYER_SHOOT_SPEED

        def draw (self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2) 
    
        def update(self, dt):
            self.position.x += (self.velocity.x * dt)
            self.position.y += (self.velocity.y * dt)
            #print(self.velocity)
            #print(self.angle)