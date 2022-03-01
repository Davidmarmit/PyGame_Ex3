import pygame


class Footprint(object):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.face = pygame.image.load('images/footprint.png')
        self.face = pygame.transform.scale(self.face, (70, 70))