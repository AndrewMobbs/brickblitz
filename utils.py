import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

BALL_RADIUS = 10
BALL_SPEED = 5

BAT_WIDTH = 100
BAT_HEIGHT = 20
BAT_SPEED = 7

BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_PADDING = 10
BRICK_ROWS = 5
BRICK_COLS = 10

RAINBOW_COLORS = [
    (200, 100, 100),       # Muted Red
    (255, 150, 100),       # Muted Orange
    (200, 200, 100),       # Muted Yellow
    (100, 200, 100),       # Muted Green
    (100, 100, 200),       # Muted Blue
    (100, 100, 150),       # Muted Indigo
    (150, 100, 200),       # Muted Violet
    (255, 180, 150),       # Muted Orange-Red
    (200, 100, 180),       # Muted Deep Pink
    (150, 200, 200),       # Muted Cyan
    (150, 100, 150),       # Muted Purple
    (200, 200, 100)        # Muted Yellow (repeated for completeness)
]
