import pygame


# Class Footprint
class Footprint(object):
    # Definition of Footprint class, responsible for the footprint images behind the character
    def __init__(self, screen, x, y, angle):
        self.screen = screen
        self.x = x
        self.y = y
        self.fp = pygame.image.load("images/footprint.png").convert_alpha()
        self.fp = pygame.transform.scale(self.fp, (70, 70))
        self.fp = pygame.transform.rotate(self.fp, angle)
        self.update_fp()

    # Definition of update_fp, which updates the character's footprint whenever needed
    def update_fp(self):
        self.screen.blit(self.fp, (self.x, self.y))

    # Definition of apply_tranparency, which updates the transparency of the footprint image according to the
    # player's movement
    def apply_transparency(self, num):
        alpha = 0
        if num == 1:
            alpha = 200
        elif num == 2:
            alpha = 150
        elif num == 3:
            alpha = 130
        elif num == 4:
            alpha = 110

        self.fp.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        self.screen.blit(self.fp, (self.x, self.y))
