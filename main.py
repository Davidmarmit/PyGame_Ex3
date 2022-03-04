import pygame

from Player import Player


# Function that loads and sets the background image
def set_background():
    pass
    background = pygame.image.load("images/mazeOK.png").convert_alpha()
    background = pygame.transform.scale(background, (1000, 1000))
    screen.blit(background, (0, 0))


# Main function
if __name__ == '__main__':
    pygame.init()

    # Main settings for the game screen
    pygame.display.set_caption("INOTIME_3")
    screen_width = 1000
    screen_high = 800
    screen = pygame.display.set_mode([screen_width, screen_high])

    # Player's starting position
    player = Player(screen, 10, 715)

    # Setting the game's icon
    icon = pygame.image.load("images/logo.png").convert_alpha()
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    # Starting the game
    running = True
    while running:
        # Looking for the user's actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player.handle_keys()
            pygame.display.update()

    clock.tick(30)
pygame.quit()
