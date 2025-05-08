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
        self.level = 1
        self.lives_balls = [Ball() for _ in range(self.lives)]

        # Initialize font for rendering text
        self.font = pygame.font.SysFont(None, 36)

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
        self.score=self.ball.update(self.bat, self.bricks, self.score)
        self.check_game_over()

    def draw(self):
        self.screen.clear()
        self.bricks.draw(self.screen.surface)
        self.bat.draw(self.screen.surface)
        self.ball.draw(self.screen.surface)

        # Draw score and lives text
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.surface.blit(score_text, (10, 10))

        # Draw lives as ball icons
        lives_label = self.font.render("Lives:", True, (255, 255, 255))
        self.screen.surface.blit(lives_label, (SCREEN_WIDTH - 220, 10))
        for i, ball in enumerate(self.lives_balls):
            ball.rect.x = SCREEN_WIDTH - 180 + i * 30
            ball.rect.y = 10
            ball.draw(self.screen.surface)
        
        # Draw level and score
        level_text = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        self.screen.surface.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 10))

        self.screen.update()

    def check_game_over(self):
        if self.ball.rect.top > SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives <= 0:
                self.running=False
            self.ball.reset()
            self.lives_balls = [Ball() for _ in range(self.lives)]

        if self.bricks.count == 0:
            self.next_level()
            return  # Exit immediately to prevent further updates

    def next_level(self):
        """Progress to the next level with increased difficulty"""
        self.level += 1
        self.bricks = Bricks(BRICK_ROWS, BRICK_COLS)
        self.ball.speed += 1  # Increase speed
        self.ball.reset()
