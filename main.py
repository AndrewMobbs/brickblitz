import pygame
from game import Game
from screen import Screen
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LOGO_COLORS, LOGO

def logo_font():
    """Attempt to find a modern monospaced font for the logo"""
    fonts=pygame.font.get_fonts()
    for i in ["liberationmono","consolas","lucidasanstypewriter"]:
        if i in fonts:
            return i
    # Couldn't find a preferred font, YOLO something
    for i in fonts:
        if "mono" in i or "typewriter" in i:
            return i
    return None

def show_splash_screen(screen, message_lines):
    """Display a splash screen with given message lines, waiting for space to continue."""

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.clear()
        font = pygame.font.SysFont(logo_font(), 12)
        for i, line in enumerate(LOGO):
            text = font.render(line, True, LOGO_COLORS[i])
            screen.surface.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 20 + i*12))        
        font = pygame.font.SysFont("liberationsans", 36)
        for i, line in enumerate(message_lines):
            text = font.render(line, True, (255, 255, 255))
            screen.surface.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 140 + i * 40))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
    return not running

if __name__ == "__main__":
    screen=Screen()
 
    # Start screen
    start_lines = ["Press SPACE to start the game"]
    show_splash_screen(screen, start_lines)

    game = Game(screen)
    game.run()

    game_over_lines = [
        "Game over!",
        f"You scored {game.score}",
        "Press SPACE to exit the game"
    ]
    show_splash_screen(screen, game_over_lines)
    exit(0)