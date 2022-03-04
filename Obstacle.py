import pygame


# Class Obstacle
class Obstacle(pygame.sprite.Sprite):
    # Definition of Obstacle, borders or rectangles the users shouldn't be able to cross
    def __init__(self, screen, size_x, size_y, pos_x, pos_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen
        self.image = pygame.image.load("images/black.jpg").convert()
        self.image = pygame.transform.scale(self.image, (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.update_obstacle()

    # Definition of update_obstacles, function that updates obstacles
    def update_obstacle(self):
        self.screen.blit(self.image, (self.pos_x, self.pos_y))
        pixel_rect = self.image.get_bounding_rect()
        trimmed_surface = pygame.Surface(pixel_rect.size)
        trimmed_surface.blit(self.screen, (0, 0), pixel_rect)
