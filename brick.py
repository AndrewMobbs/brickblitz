import pygame
import random
from constants import BRICK_WIDTH, BRICK_HEIGHT, BRICK_PADDING, SCREEN_WIDTH, BRICK_COLORS

class Bricks:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.bricks = self.create_bricks()
        self.count = len(self.bricks)

    def create_bricks(self):
        bricks = []
        prev_row_colors = None
        for row in range(self.rows):
            # Offset every other row for stretcher bond pattern
            offset = BRICK_WIDTH // 2 if row % 2 == 0 else 0
            current_row_colors = []
            for col in range(self.cols):
                brick_x = col * (BRICK_WIDTH + BRICK_PADDING) + offset
                brick_y = row * (BRICK_HEIGHT + BRICK_PADDING) + 50
                rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
                
                # Determine forbidden colors
                forbidden_colors = set()
                if col > 0:
                    forbidden_colors.add(current_row_colors[-1])
                if row > 0:
                    forbidden_colors.add(prev_row_colors[col])
                
                # Choose a color not in forbidden_colors
                color = None
                while color is None or color in forbidden_colors:
                    color = random.choice(BRICK_COLORS)
                
                current_row_colors.append(color)
                if rect.right <= SCREEN_WIDTH:
                    bricks.append({'rect': rect, 'color': color})
            prev_row_colors = current_row_colors
        return bricks

    def draw(self, surface):
        for brick in self.bricks:
            pygame.draw.rect(surface, brick['color'], brick['rect'])

    def remove(self, brick):
        self.bricks.remove(brick)
        self.count -= 1
