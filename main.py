import pygame
from game import Game
from utils import SCREEN_WIDTH, SCREEN_HEIGHT

def show_splash_screen(screen, font, message_lines):
    """Display a splash screen with given message lines, waiting for space to continue."""
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0, 0, 0))
        for i, line in enumerate(message_lines):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 50 + i * 40))
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
    
    def show_splash_screen(screen, font, message_lines):
        """Display a splash screen with given message lines, waiting for space to continue."""
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill((0, 0, 0))
            for i, line in enumerate(message_lines):
                text = font.render(line, True, (255, 255, 255))
                screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 50 + i * 40))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    running = False
        return not running

    # Constants
    LOGO_LINES = [
        "    _____           _       _     _          ",
        "   /  ___|         | |     | |   (_)         ",
        "   \\ `--.  ___  ___| |__   | |    _  _ __ ___ ",
        "    `--. \\/ _ \\/ __| '_ \\  | |   | || '_ ` _ \\",
        "  .___/\\/\\/\\_\\___|_| |_| |_|   |_|_|_| |_| |_/",
    ]

    # Start screen
    font = pygame.font.SysFont("Comic Sans MS", 36)
    start_lines = LOGO_LINES + [
        "                                              ",
        "         Press SPACE to start the game        "
    ]
    show_splash_screen(screen, font, start_lines)
    
    pygame.display.set_caption("Breakout")
    game = Game()
    game.run()

    if game.game_over:
        font = pygame.font.SysFont("Comic Sans MS", 36)
        game_over_lines = LOGO_LINES + [
            " ",
            "Game over!",
            f"You scored {game.score}",
            "Press SPACE to exit the game"
        ]
        show_splash_screen(screen, font, game_over_lines)
