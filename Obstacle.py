import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (0, 0, 10000, 100))
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (0, 0, 100, 700))
        self.rect = pygame.draw.rect(screen, (0, 128, 128), (400, 0, 100, 400))

