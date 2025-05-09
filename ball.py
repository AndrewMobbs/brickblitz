import pygame
from constants import BALL_RADIUS, BALL_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_COLORS

class Ball:
    def __init__(self):
        self.radius = BALL_RADIUS
        self.speed = BALL_SPEED
        self.collision_counter = 0 # avoid being "trapped" on the bat with repeated collisions
        self.ball_surface=self._pre_render_ball()
        self.reset()
        
    def _pre_render_ball(self):
        # Create a transparent surface for the ball
        ball_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        ball_center_on_surface = (self.radius, self.radius)

        # Draw main ball body
        pygame.draw.circle(ball_surface, BALL_COLORS[0], ball_center_on_surface, self.radius)

        # Draw smooth specular highlight gradient
        # Adjusting center for the ball_surface (origin is 0,0 for this surface)
        highlight_base_x = ball_center_on_surface[0]
        highlight_base_y = ball_center_on_surface[1]

        for i in range(2, 5):
            offset_x = self.radius // (12 - 2 * i)
            offset_y = self.radius // (12 - 2 * i)
            highlight_radius = self.radius // i
            pygame.draw.circle(ball_surface, BALL_COLORS[i-1],
                               (highlight_base_x - offset_x, highlight_base_y - offset_y),
                               highlight_radius)
        return ball_surface

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
        surface.blit(self.ball_surface, self.rect.topleft)

