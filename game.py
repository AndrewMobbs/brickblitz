import pygame
from ball import Ball
from bat import Bat
from brick import Bricks
from screen import Screen
from utils import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BRICK_ROWS, BRICK_COLS

class Game:
    def __init__(self):
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.running = True

        self.ball = Ball()
        self.bat = Bat()
        self.bricks = Bricks(BRICK_ROWS, BRICK_COLS)

        self.score = 0
        self.lives = 3

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.bat.update()
        self.ball.update(self.bat, self.bricks, self.score)
        self.check_game_over()

    def draw(self):
        self.screen.clear()
        self.bricks.draw(self.screen.surface)
        self.bat.draw(self.screen.surface)
        self.ball.draw(self.screen.surface)
        self.screen.update()

    def check_game_over(self):
        if self.ball.rect.top > SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives <= 0:
                self.running = False
            self.ball.reset()

        if self.bricks.count == 0:
            self.running = False
