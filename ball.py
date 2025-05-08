import pygame
from utils import BALL_RADIUS, BALL_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Ball:
    def __init__(self):
        self.radius = BALL_RADIUS
        self.speed = BALL_SPEED
        self.collision_counter = 0 # avoid being "trapped" on the bat with repeated collisions
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - self.radius, SCREEN_HEIGHT // 2 - self.radius, self.radius * 2, self.radius * 2)
        self.dx = self.speed
        self.dy = -self.speed

    def update(self, bat, bricks, score):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.collision_counter > 0:
            self.collision_counter -= 1

        # Wall collisions
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.dx *= -1
        if self.rect.top <= 0:
            self.dy *= -1

        # Bat collision
        if self.rect.colliderect(bat.rect) and self.collision_counter == 0:
            self.dy *= -1
            self.collision_counter = 10

        # Brick collision
        for brick in bricks.bricks:
            if self.rect.colliderect(brick['rect']):
                bricks.remove(brick)
                score += 1
                self.dy *= -1
                break
        return score

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.rect.center, self.radius)
