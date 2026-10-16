import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
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
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(angle)
            velocity_2 = self.velocity.rotate(-angle)
            radius_1 = self.radius - ASTEROID_MIN_RADIUS
            radius_2 = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, radius_1)
            asteroid_2 = Asteroid(self.position.x, self.position.y, radius_2)
            asteroid_1.velocity = velocity_1 * 1.2
            asteroid_2.velocity = velocity_2 * 1.2
