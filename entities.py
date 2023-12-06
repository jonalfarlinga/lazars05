import pygame
from os import path
from vector_math import raycast_DDA
from constants import *  # noqa:F403 flake8 ignore


class Player():
    rect = pygame.Rect(0, 0, 1, 1)
    image_src = path.join("assets", "player.png")
    image = pygame.image.load(image_src)
    rect = image.get_rect()
    direction = 0  # facing in radians
    speed = 5  # number of times to move per frame
    bounces = 3  # number of times to bounce the laser

    def find_bounce(self, game_map):
        return [raycast_DDA(
            self.rect.center,
            self.direction,
            game_map,
        )]

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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction -= 2.5
            if self.direction < 0:
                self.direction += 360
        if keys[pygame.K_LEFT]:
            self.direction += 2.5
            if self.direction > 359:
                self.direction -= 360
