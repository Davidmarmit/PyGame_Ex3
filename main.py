import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("INOTIME_3")

    screen_witdh = 1000
    screen_heigt = 1000

    screen = pygame.display.set_mode([screen_witdh, screen_heigt])

    icon = pygame.image.load("logo.png").convert_alpha()
    pygame.display.set_icon(icon)

    bkgd = pygame.image.load("mazeOK.png").convert_alpha()
    bkgd = pygame.transform.scale(bkgd, (1000, 1000))
    screen.blit(bkgd, (0,0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()