import pygame

from Obstacle import Obstacle


# class Player
class Player(pygame.sprite.Sprite):
    # constructor Player: needs display, and start position
    def __init__(self, screen, x, y):
        # super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.face = pygame.image.load('images/player.png')
        self.face = pygame.transform.scale(self.face, (70, 70))
        self.x = x
        self.y = y
        self.obstacles = pygame.sprite.Group()

        self.footprints = []
        self.rect = self.face.get_rect()
        self.load_player()

    def load_player(self):
        self.set_background()
        obstacle = Obstacle(self.screen, 1000, 100)
        obstacle2 = Obstacle(self.screen, 100, 700)
        self.obstacles.add(obstacle)
        self.obstacles.add(obstacle2)

        self.screen.blit(self.face, (self.x, self.y))
        pygame.display.flip()
        pygame.display.update()

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.move_ip(self.x - 50, self.y)
            if not self.collide_obstacle():
                self.set_background()
                self.x += 50
                self.set_footprints(90)  # angle rotation
                self.x -= 100
                self.screen.blit(self.face, (self.x, self.y))
            else:
                self.rect.move_ip(self.x + 50, self.y)
        if key[pygame.K_RIGHT]:
            if not self.collide_obstacle():
                self.set_background()
                self.x -= 50
                self.set_footprints(-90)
                self.x += 80
                self.screen.blit(self.face, (self.x, self.y))
        if key[pygame.K_UP]:
            self.y -= 50
            #self.rect.move_ip(self.x, self.y)
            if not self.collide_obstacle():
                print("bien")
                self.set_background()
                # self.y += 50
                # self.set_footprints(360)
                # self.y -= 100
                self.screen.blit(self.face, (self.x, self.y))
            else:
                pass
                #self.y += 50
                #self.rect.move_ip(self.x, self.y)

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
        self.update_obstacles()  # update obstacles

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update_obstacle()

    # if player collides with any obstacle
    def collide_obstacle(self):
        collide = False
        # if pygame.sprite.spritecollideany(self, self.obstacles):
        if pygame.sprite.spritecollide(self, self.obstacles, False):
            print("collide")
            collide = True

        return collide
