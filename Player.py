import time

import pygame

from Footprint import Footprint
from Obstacle import Obstacle
from Goal import Goal


# class Player
class Player(pygame.sprite.Sprite):
    # constructor Player: needs display, and start position
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y

        # initializes player image, scales it, and masks it
        self.image = pygame.image.load('images/player_shadow.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.mask_face = pygame.mask.from_surface(self.image)

        # sets the image rect to the same position as the image:
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # initializes player image and scales it:
        self.player_ko = pygame.image.load('images/player_ko.png')
        self.player_ko = pygame.transform.scale(self.player_ko, (70, 70))

        # creates sprite groups:
        self.obstacles = pygame.sprite.Group()
        self.goal_sprite = pygame.sprite.Group()
        self.goal = Goal(self.screen, 900, 700)
        self.goal_sprite.add(self.goal)

        self.footprints = []
        self.current_map1 = True
        self.load_map1()  # load map of obstacles

        # initialize sounds
        self.walk_sound = pygame.mixer.Sound("sounds/jumps.wav")
        self.collide_sound = pygame.mixer.Sound("sounds/boom.wav")
        self.win_sound = pygame.mixer.Sound("sounds/win.wav")

    # Function that creates the obstacles in the map's game
    # We define obstacles such as rectangles inside the map that define the labyrinth and the map's borders
    # These are for the first map
    def create_obstacles_map1(self):
        self.current_map1 = True
        self.obstacles = pygame.sprite.Group()
        self.obstacles.add(Obstacle(self.screen, 1000, 100, 0, 800))  # margin display Bottom
        self.obstacles.add(Obstacle(self.screen, 100, 1000, -100, -100))  # margin display left

        self.obstacles.add(Obstacle(self.screen, 1000, 100, 0, 0))  # Horizontal top
        self.obstacles.add(Obstacle(self.screen, 100, 700, 0, 0))  # Vertical left

        self.obstacles.add(Obstacle(self.screen, 600, 100, 200, 200))  # Horizontal center-top
        self.obstacles.add(Obstacle(self.screen, 100, 700, 200, 300))  # Vertical center-left

        self.obstacles.add(Obstacle(self.screen, 100, 700, 900, 0))  # Vertical right

        self.obstacles.add(Obstacle(self.screen, 100, 300, 600, 400))
        self.obstacles.add(Obstacle(self.screen, 100, 300, 400, 600))
        self.obstacles.add(Obstacle(self.screen, 100, 100, 700, 600))
        self.obstacles.add(Obstacle(self.screen, 500, 100, 400, 400))  # Horizontal center bottom

    # Function that creates the obstacles in the map's game
    # We define obstacles such as rectangles inside the map that define the labyrinth and the map's borders
    # These are for the second map
    def create_obstacles_map2(self):
        self.current_map1 = False
        self.obstacles = pygame.sprite.Group()
        self.obstacles.add(Obstacle(self.screen, 1000, 100, 0, 800))  # margin display Bottom
        self.obstacles.add(Obstacle(self.screen, 100, 1000, -100, -100))  # margin display left

        self.obstacles.add(Obstacle(self.screen, 1000, 100, 0, 0))  # Horizontal top
        self.obstacles.add(Obstacle(self.screen, 100, 700, 0, 0))  # Vertical left

        self.obstacles.add(Obstacle(self.screen, 600, 100, 200, 200))  # Horizontal center-top
        self.obstacles.add(Obstacle(self.screen, 100, 400, 200, 300))  # Vertical center-left

        self.obstacles.add(Obstacle(self.screen, 100, 700, 900, 200))  # Vertical right
        self.obstacles.add(Obstacle(self.screen, 100, 200, 700, 100))
        self.obstacles.add(Obstacle(self.screen, 100, 300, 600, 400))
        self.obstacles.add(Obstacle(self.screen, 100, 300, 400, 600))
        self.obstacles.add(Obstacle(self.screen, 100, 100, 700, 600))
        self.obstacles.add(Obstacle(self.screen, 500, 100, 400, 400))  # Horizontal center bottom

    # settings to use map1:
    def load_map1(self):
        self.footprints = []
        self.goal_sprite = pygame.sprite.Group()
        self.goal = Goal(self.screen, 900, 700)
        self.goal_sprite.add(self.goal)
        self.create_obstacles_map1()
        self.set_background()
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        pygame.display.update()

    # settings to use map2:
    def load_map2(self):
        self.footprints = []
        self.goal_sprite = pygame.sprite.Group()
        self.goal = Goal(self.screen, 900, 100)
        self.goal_sprite.add(self.goal)
        self.create_obstacles_map2()
        self.set_background()

        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        pygame.display.update()

    # Function to load the player_ko image when a collision occurred
    def load_player_ko(self):
        self.screen.blit(self.player_ko, (self.x, self.y))

    # Function to execute the actions needed when the player uses the corresponding keys, such as arrow up, down,
    # left, right.
    def handle_keys(self):

        # We look for the key that has been pressed
        key = pygame.key.get_pressed()

        # Left arrow key
        if key[pygame.K_LEFT]:
            self.move_left()
            collide = False

            # Check for collisions
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask)
            if len(list_collide):
                pygame.mixer.Sound.play(self.collide_sound)
                collide = True
            if not collide:
                pygame.mixer.Sound.play(self.walk_sound)
                self.set_background()
                self.x += 50
                self.set_footprints(+90)
                self.x -= 100
                self.screen.blit(self.image, (self.x, self.y))
            else:
                self.set_background()
                self.move_right()
                self.load_player_ko()

        # Right arrow key
        if key[pygame.K_RIGHT]:
            self.move_right()
            collide = False
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask)
            if len(list_collide):

                pygame.mixer.Sound.play(self.collide_sound)
                collide = True
            if not collide:
                list_win = pygame.sprite.spritecollide(self, self.goal_sprite, False)
                self.set_background()
                self.x -= 50
                self.set_footprints(-90)
                self.x += 100
                self.screen.blit(self.image, (self.x, self.y))
                if len(list_win):
                    pygame.mixer.Sound.play(self.win_sound)
                    pygame.display.update()  # Update per ficar el personatge dins la casella de victoria
                    time.sleep(2)
                    self.x = 10
                    self.y = 715
                    if self.current_map1:
                        self.load_map2()
                    else:
                        self.load_map1()
                else:
                    pygame.mixer.Sound.play(self.walk_sound)

            else:
                self.set_background()
                self.move_left()
                self.load_player_ko()

        # Up arrow key
        if key[pygame.K_UP]:
            self.move_up()
            collide = False
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask)
            if len(list_collide):
                pygame.mixer.Sound.play(self.collide_sound)
                collide = True
            if not collide:
                pygame.mixer.Sound.play(self.walk_sound)
                self.set_background()
                self.y += 50
                self.set_footprints(360)
                self.y -= 100
                self.screen.blit(self.image, (self.x, self.y))
            else:
                self.set_background()
                self.move_down()
                self.load_player_ko()

        # Down arrow key
        if key[pygame.K_DOWN]:
            self.move_down()
            collide = False
            list_collide = pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask)
            if len(list_collide):
                pygame.mixer.Sound.play(self.collide_sound)
                collide = True
            if not collide:
                pygame.mixer.Sound.play(self.walk_sound)
                self.set_background()
                self.y -= 50
                self.set_footprints(180)
                self.y += 100
                self.screen.blit(self.image, (self.x, self.y))
            else:
                self.set_background()
                self.move_up()
                self.load_player_ko()

    # Function that sets the main characters footprints on the correct angle
    def set_footprints(self, angle):
        # footprint = pygame.image.load("images/footprint.png").convert_alpha()
        # footprint = pygame.transform.scale(footprint, (70, 70))
        # footprint = pygame.transform.rotate(footprint, angle)
        fp = Footprint(self.screen, self.x, self.y, angle)
        self.footprints.append(fp)
        self.update_footprints()

    # Function that updates all the footprints that have been created with the correct opacity to create the fading
    # effect
    def update_footprints(self):
        cont = len(self.footprints)
        if cont > 1:
            cont = len(self.footprints) - 1
            num_fp = 1
            while cont >= 0:
                self.footprints[cont].apply_transparency(num_fp)
                cont -= 1
                num_fp += 1

    # Function that sets the background
    def set_background(self):
        background = pygame.image.load("images/background.jpg").convert()
        background = pygame.transform.scale(background, (1000, 800))
        self.screen.blit(background, (0, 0))
        self.update_boxes()

    # update obstacles and goal
    def update_boxes(self):
        self.goal.update_goal()
        for obstacle in self.obstacles:
            obstacle.update_obstacle()

    # Function that moves up the character
    def move_up(self):
        self.y -= 50
        self.screen.blit(self.image, (self.x, self.y))
        self.update_rect()

    # Function that moves down the character
    def move_down(self):
        self.y += 50
        self.screen.blit(self.image, (self.x, self.y))
        self.update_rect()
        # pygame.draw.rect(self.screen, (0, 0, 0), self.rect)

    # Function that moves left the character
    def move_left(self):
        self.x -= 50
        self.screen.blit(self.image, (self.x, self.y))
        self.update_rect()

    # Function that moves right the character
    def move_right(self):
        self.x += 50
        self.screen.blit(self.image, (self.x, self.y))
        self.update_rect()

    # Function that updates the character (setting it to x position)
    def update_rect(self):
        self.rect.x = self.x
        self.rect.y = self.y
