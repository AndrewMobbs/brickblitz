import pygame
import random
from utils import BRICK_WIDTH, BRICK_HEIGHT, BRICK_PADDING, BRICK_ROWS, BRICK_COLS, SCREEN_WIDTH, SCREEN_HEIGHT

class Bricks:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.bricks = self.create_bricks()
        self.count = len(self.bricks)

    def create_bricks(self):
        bricks = []
        for row in range(self.rows):
            # Offset every other row for stretcher bond pattern
            offset = BRICK_WIDTH // 2 if row % 2 == 0 else 0
            for col in range(self.cols):
                brick_x = col * (BRICK_WIDTH + BRICK_PADDING) + offset
                brick_y = row * (BRICK_HEIGHT + BRICK_PADDING) + 50
                rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
                color = random.choice(RAINBOW_COLORS)
                bricks.append({'rect': rect, 'color': color})
        return bricks

    def draw(self, surface):
        for brick in self.bricks:
            pygame.draw.rect(surface, brick['color'], brick['rect'])

    def remove(self, brick):
        self.bricks.remove(brick)
        self.count -= 1
