import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen, size_x, size_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.screen = screen
        self.image = pygame.Surface((size_x, size_y))
        self.image.fill((0, 0, 128))
        self.rect = self.image.get_rect()
        self.update_obstacle()

    def update_obstacle(self):
        self.screen.blit(self.image, (0, 0))
