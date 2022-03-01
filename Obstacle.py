import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen, size_x, size_y):
        super().__init__()
        self.wall = pygame.Surface((size_x, size_y))
        self.wall.fill((0, 0, 128))
        self.screen = screen
        self.rect = self.wall.get_rect()
        self.screen.blit(self.wall, (0, 0))
        #pygame.draw.rect(screen, (0, 0, 128), (0, 0, size_x, size_y))
