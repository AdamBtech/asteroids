import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position[0], position[1], SHOT_RADIUS)

        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt
