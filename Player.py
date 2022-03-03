import pygame

from Obstacle import Obstacle
from Goal import Goal


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
        self.goal = Goal(self.screen)
        self.footprints = []
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.load_player()
        self.walk_sound = pygame.mixer.Sound("sounds/jumps.wav")
        self.collide_sound = pygame.mixer.Sound("sounds/boom.wav")
        self.win_sound = pygame.mixer.Sound("sounds/win.wav")


    def create_obstacles(self):
        self.obstacles.add(Obstacle(self.screen, 1000, 100, 0, 800))  # margin display Bottom
        self.obstacles.add(Obstacle(self.screen, 100, 1000, -100, -100))  # margin display left
        self.obstacles.add(Obstacle(self.screen, 1000, 100, 0, 0))  # H
        self.obstacles.add(Obstacle(self.screen, 100, 700, 0, 0))
        self.obstacles.add(Obstacle(self.screen, 600, 100, 200, 200))
        self.obstacles.add(Obstacle(self.screen, 100, 700, 200, 300))
        self.obstacles.add(Obstacle(self.screen, 100, 700, 900, 0))
        self.obstacles.add(Obstacle(self.screen, 1000, 100, 400, 400))  # H
        self.obstacles.add(Obstacle(self.screen, 100, 200, 400, 400))
        self.obstacles.add(Obstacle(self.screen, 100, 200, 600, 400))
        self.obstacles.add(Obstacle(self.screen, 100, 200, 400, 700))

    def load_player(self):
        self.set_background()
        self.create_obstacles()
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        pygame.display.update()

    def handle_keys(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move_left()
            collide = False
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask)
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
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask)
            if len(list_collide):
                print("collide")
                pygame.mixer.Sound.play(self.collide_sound)
                collide = True
            if not collide:
                print("bien")
                pygame.mixer.Sound.play(self.walk_sound)
                pygame.mixer.Sound.play(self.walk_sound)
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
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask)
            if len(list_collide):
                print("collide")
                pygame.mixer.Sound.play(self.collide_sound)
                collide = True
            if not collide:
                print("bien")
                pygame.mixer.Sound.play(self.walk_sound)
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
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask)
            if len(list_collide):
                print("collide")
                pygame.mixer.Sound.play(self.collide_sound)
                collide = True
            if not collide:
                print("bien")
                pygame.mixer.Sound.play(self.walk_sound)
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
        self.update_boxes()  # update obstacles

    def update_boxes(self):
        self.goal.update_goal()
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
