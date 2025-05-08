import pygame
from utils import BAT_WIDTH, BAT_HEIGHT, BAT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Bat:
    def __init__(self):
        self.width = BAT_WIDTH
        self.height = BAT_HEIGHT
        self.speed = BAT_SPEED
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - self.width // 2, SCREEN_HEIGHT - self.height - 10, self.width, self.height)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        # Draw main body with rounded corners
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        # Draw shading for brushed steel effect
        pygame.draw.rect(surface, (120, 120, 120), (self.rect.x + 5, self.rect.y + 5, self.rect.width - 10, self.rect.height - 10), border_radius=5)
