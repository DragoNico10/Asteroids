import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand = random.uniform(20, 50)
        rot1 = self.velocity.rotate(rand)
        rot2 = self.velocity.rotate(0 - rand)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], new_rad)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_rad)
        asteroid1.velocity = rot1 * 1.2
        asteroid2.velocity = rot2 * 1.2
