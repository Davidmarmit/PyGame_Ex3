import pygame


class Goal(pygame.sprite.Sprite):
    def __init__(self, screen, pos_x, pos_y):
        super().__init__()
        self.size_x = 100
        self.size_y = 100
        self.pos_x = pos_x  # map1= 900
        self.pos_y = pos_y  # map1= 700
        self.screen = screen
        self.image = pygame.image.load("images/goal.jpg").convert()
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.update_goal()
        print("o")

    def update_goal(self):
        self.screen.blit(self.image, (self.pos_x, self.pos_y))
