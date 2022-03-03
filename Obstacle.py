import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen, size_x, size_y, pos_x, pos_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen
        self.image = pygame.Surface((size_x, size_y))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.update_obstacle()
        print("o")

    def update_obstacle(self):
        self.screen.blit(self.image, (self.pos_x, self.pos_y))
