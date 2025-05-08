import pygame
from game import Game

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Brick Blitz")
    
    # Splash screen
    font = pygame.font.SysFont("Comic Sans MS", 36)
    lines = [
        "    _____           _       _     _          ",
        "   /  ___|         | |     | |   (_)         ",
        "   \\ `--.  ___  ___| |__   | |    _  _ __ ___ ",
        "    `--. \\/ _ \\/ __| '_ \\  | |   | || '_ ` _ \\",
        "  .___/\\/\\/\\_\\___|_| |_| |_|   |_|_|_| |_| |_/",
        "                                              ",
        "         Press SPACE to start the game        "
    ]
    
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0, 0, 0))
        for i, line in enumerate(lines):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 50 + i * 40))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
    
    pygame.display.set_caption("Breakout")
    game = Game()
    game.run()
