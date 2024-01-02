import pygame
from os import path
from vector_math import raycast_DDA, deg_to_vector
from constants import *  # noqa:F403 flake8 ignore
DEBUG = False


class Player():
    image_src = path.join("assets", "player.png")
    image = pygame.image.load(image_src)
    rect = image.get_rect()
    direction = 355  # facing in radians
    speed = 5  # number of times to move per frame
    bounces = 3  # number of times to bounce the laser

    def find_bounce(self, game_map):
        global DEBUG
        bounce_points = []
        vector = self.direction
        source = self.rect.center

        while len(bounce_points) < self.bounces:
            source, vector = raycast_DDA(
                source,
                vector,
                game_map,
            )
            if DEBUG:
                DEBUG = False
                print(source)
            bounce_points.append(source)

        return bounce_points

    # find laser bounces and blit lines
    def laser(self, screen, map):
        # calculate bounce pints
        bounce_points = self.find_bounce(map)

        # origin starts at player position
        origin = self.rect.center

        # for each bounce point
        for point in bounce_points:
            # draw a line from origin to bounce
            pygame.draw.aaline(
                screen,
                LASER,
                origin,
                point,
                # width=3,
            )
            # set new origin at previous bounce
            origin = point

    def action(self):
        global DEBUG
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            DEBUG = True
            self.direction -= 2.5
            print(self.direction, deg_to_vector(self.direction))
            if self.direction < 0:
                self.direction += 360
        if keys[pygame.K_RIGHT]:
            DEBUG = True
            print(self.direction, deg_to_vector(self.direction))
            self.direction += 2.5
            if self.direction > 359:
                self.direction -= 360
