import pygame

from Obstacle import Obstacle
from Player import Player


def set_background():
    background = pygame.image.load("images/mazeOK.png").convert_alpha()
    background = pygame.transform.scale(background, (1000, 1000))
    screen.blit(background, (0, 0))


if __name__ == '__main__':
    pygame.init()
    # BASIC  display CONFIG PYGAME:
    pygame.display.set_caption("INOTIME_3")
    screen_width = 1000
    screen_high = 800
    screen = pygame.display.set_mode([screen_width, screen_high])

    set_background()
    player = Player(screen, 0, 715)


    icon = pygame.image.load("images/logo.png").convert_alpha()
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.handle_keys()

        pygame.display.update()

    clock.tick(40)
pygame.quit()
