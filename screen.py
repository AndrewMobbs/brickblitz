import pygame
from utils import SCREEN_WIDTH, SCREEN_HEIGHT

class Screen:
    def __init__(self):
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")

    def clear(self):
        self.surface.fill((0, 0, 0))

    def update(self):
        pygame.display.flip()
