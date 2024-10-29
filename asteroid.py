import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Pass radius to parent constructor
        self.velocity = pygame.math.Vector2(0, 0)  # Initialize velocity

    def draw(self, screen):
        pygame.draw.circle(
            screen, WHITE, (int(self.position.x), int(self.position.y)), self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.uniform(20, 50)
        angle1 = self.velocity.rotate(random_angle) * 1.2
        angle2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position, angle1, new_radius)
        new_asteroid1.velocity = angle1
        new_asteroid2 = Asteroid(self.position, angle2, new_radius)
        new_asteroid2.velocity = angle2
