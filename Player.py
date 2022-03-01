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
        self.obstacles = pygame.sprite.Group()
        self.load_player()
        self.footprints = []
        self.rect = self.face.get_rect()

    def load_player(self):
        self.set_background()
        self.screen.blit(self.face, (self.x, self.y))
        pygame.display.flip()
        pygame.display.update()

    def handle_keys(self):
        key = pygame.key.get_pressed()
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
            if not self.collides_obstacle():
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
        self.create_obstacles()

    def create_obstacles(self):
        # self.rect3 = pygame.draw.rect(screen, (0, 128, 128), (400, 0, 100, 400))
        obstacle = Obstacle(self.screen, 10000, 100)
        obstacle2 = Obstacle(self.screen, 100, 500)
        self.obstacles.add(Obstacle(self.screen, 10000, 100))
        self.obstacles.add(Obstacle(self.screen, 100, 500))

    # surface fill get rect
    def collides_obstacle(self):
        collide = False
        for obstacle in self.obstacles:
            # if self.rect.colliderect(obstacle):
            if pygame.sprite.spritecollideany(self, self.obstacles):
                print("a")
                collide = True

        return collide

        # if pygame.sprite.spritecollide(self, self.obstacles, False):
        #   return True
        # return False
