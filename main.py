import pygame
from game import Game
from utils import SCREEN_WIDTH, SCREEN_HEIGHT

def show_splash_screen(screen, message_lines):
    """Display a splash screen with given message lines, waiting for space to continue."""
    LOGO_LINES = [
"░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░ ",
"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░          ░▒▓█▓▒░ ",
"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░        ░▒▓██▓▒░  ",
"░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓██▓▒░    ",
"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓██▓▒░      ",
"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        ",
"░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░ "   ]
    logo_color = [(255,211,25),(255,178,28),(255,144,31),(255,41,117),(242,34,255),(191,32,255),(140,30,255)]
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("liberationmono", 12)
        for i, line in enumerate(LOGO_LINES):
            text = font.render(line, True, logo_color[i])
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 20 + i*12))        
        font = pygame.font.SysFont("liberationsans", 36)
        for i, line in enumerate(message_lines):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 100 + i * 40))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
    return not running

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Brick Blitz")

    # Start screen
    start_lines = [
        " ",
        "Press SPACE to start the game"
    ]
    show_splash_screen(screen, start_lines)
    
    pygame.display.set_caption("Breakout")
    game = Game()
    game.run()

    game_over_lines = [
        " ",
        "Game over!",
        f"You scored {game.score}",
        "Press SPACE to exit the game"
    ]
    show_splash_screen(screen, game_over_lines)
    exit(0)