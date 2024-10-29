import pygame
from constants import *


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen, WHITE, (int(self.position.x), int(self.position.y)), self.radius
        )
        pass

    def update(self, dt):
        pass

    def check_collision(self, other):
        circles_distances = self.position.distance_to(other.position)
        circles_radius = self.radius + other.radius
        if circles_distances <= circles_radius:
            return True
        return False
