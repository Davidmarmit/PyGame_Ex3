import pygame

from Obstacle import Obstacle


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.face = pygame.image.load('images/player.png')
        self.face = pygame.transform.scale(self.face, (70, 70))
        self.x = x
        self.y = y
        self.load_player()
        self.footprints = []

    def load_player(self):
        self.screen.blit(self.face, (self.x, self.y))
        pygame.display.flip()
        pygame.display.update()

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
            self.set_background()
            self.x += 50
            self.set_footprints(90)
            self.x -= 80
            self.screen.blit(self.face, (self.x, self.y))
        if key[pygame.K_RIGHT]:
            self.set_background()
            self.x -= 50
            self.set_footprints(-90)
            self.x += 80
            self.screen.blit(self.face, (self.x, self.y))
        if key[pygame.K_UP]:
            self.set_background()
            self.y += 50
            self.set_footprints(360)
            self.y -= 80
            self.screen.blit(self.face, (self.x, self.y))

        if key[pygame.K_DOWN]:
            self.set_background()
            self.y -= 50
            self.set_footprints(-180)
            self.y += 80
            self.screen.blit(self.face, (self.x, self.y))

    def set_footprints(self, angle):
        footprint = pygame.image.load("images/footprint.png").convert_alpha()
        footprint = pygame.transform.scale(footprint, (70, 70))
        footprint = pygame.transform.rotate(footprint, angle)
        self.footprints.append(footprint)
        self.screen.blit(footprint, (self.x, self.y))

    def set_background(self):
        background = pygame.image.load("images/mazeOK.png").convert_alpha()
        background = pygame.transform.scale(background, (1000, 1000))
        self.screen.blit(background, (0, 0))
        obstacle = Obstacle(self.screen)

    def collides_obstacle(self):
        obstacle = Obstacle(self.screen)

        if pygame.sprite.spritecollide(self, obstacle, False):
            return True
        return False
