import pygame
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
            for col in range(self.cols):
                brick_x = col * (BRICK_WIDTH + BRICK_PADDING)
                brick_y = row * (BRICK_HEIGHT + BRICK_PADDING) + 50
                rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
                bricks.append({'rect': rect})
        return bricks

    def draw(self, surface):
        for brick in self.bricks:
            pygame.draw.rect(surface, (100, 100, 255), brick['rect'])

    def remove(self, brick):
        self.bricks.remove(brick)
        self.count -= 1
