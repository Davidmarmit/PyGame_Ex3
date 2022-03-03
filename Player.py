import pygame

from Obstacle import Obstacle


# class Player
class Player(pygame.sprite.Sprite):
    # constructor Player: needs display, and start position
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.mask_face = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.obstacles = pygame.sprite.Group()

        self.footprints = []
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.load_player()

    def load_player(self):
        self.set_background()
        obstacle = Obstacle(self.screen, 1000, 100)
        obstacle2 = Obstacle(self.screen, 100, 700)
        self.obstacles.add(obstacle)
        self.obstacles.add(obstacle2)

        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        pygame.display.update()

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move_left()
            collide = False
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False)
            if len(list_collide):
                print("collide")
                collide = True
            if not collide:
                print("bien")
                self.set_background()
                self.x += 50
                self.set_footprints(+90)
                self.x -= 100
                self.screen.blit(self.image, (self.x, self.y))
            else:
                self.set_background()
                self.move_right()

        if key[pygame.K_RIGHT]:
            self.move_right()
            collide = False
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False)
            if len(list_collide):
                print("collide")
                collide = True
            if not collide:
                print("bien")
                self.set_background()
                self.x -= 50
                self.set_footprints(-90)
                self.x += 100
                self.screen.blit(self.image, (self.x, self.y))
            else:
                self.set_background()
                self.move_left()

        if key[pygame.K_UP]:
            self.move_up()
            collide = False
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False)
            if len(list_collide):
                print("collide")
                collide = True
            if not collide:
                print("bien")
                self.set_background()
                self.y += 50
                self.set_footprints(360)
                self.y -= 100
                self.screen.blit(self.image, (self.x, self.y))
            else:
                self.set_background()
                self.move_down()

        if key[pygame.K_DOWN]:
            self.move_down()
            collide = False
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False)
            if len(list_collide):
                print("collide")
                collide = True
            if not collide:
                print("bien")
                self.set_background()
                self.y -= 50
                self.set_footprints(180)
                self.y += 100
                self.screen.blit(self.image, (self.x, self.y))
            else:
                self.set_background()
                self.move_up()

    def set_footprints(self, angle):
        footprint = pygame.image.load("images/footprint.png").convert_alpha()
        footprint = pygame.transform.scale(footprint, (70, 70))
        footprint = pygame.transform.rotate(footprint, angle)
        self.footprints.append(footprint)
        self.screen.blit(footprint, (self.x, self.y))

    def set_background(self):
        # background = pygame.image.load("images/mazeOK.png").convert_alpha()
        # background = pygame.transform.scale(background, (1000, 1000))
        self.screen.fill((0, 120, 120))
        # self.screen.blit(background, (0, 0))
        self.update_obstacles()  # update obstacles

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update_obstacle()

    def move_up(self):
        self.y -= 50
        self.screen.blit(self.image, (self.x, self.y))
        self.update_rect()

    def move_down(self):
        self.y += 50
        self.screen.blit(self.image, (self.x, self.y))
        self.update_rect()
        # pygame.draw.rect(self.screen, (0, 0, 0), self.rect)

    def move_left(self):
        self.x -= 50
        self.screen.blit(self.image, (self.x, self.y))
        self.update_rect()

    def move_right(self):
        self.x += 50
        self.screen.blit(self.image, (self.x, self.y))
        self.update_rect()

    def update_rect(self):
        self.rect.x = self.x
        self.rect.y = self.y
