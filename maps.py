import pygame
import os
from constants import *  # noqa:F403 flake8 ignore
'''
map builders
Linting is ignored in this file for "Line is too long"
'''


class Wall(pygame.sprite.Sprite):
    def __init__(self, center=None):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "wall.png"))
        self.rect = self.image.get_rect()
        if center:
            self.rect.centerx = center[0]
            self.rect.centery = center[1]

    def blit_sprite(self, surface):
        surface.blit(
            source=self.image,
            dest=(self.rect.centerx - self.image.get_size()[0] // 2,
                  self.rect.centery - self.image.get_size()[1] // 2)
        )


def array_to_walls(array):
    walls = []
    y = BORDER_WIDTH + TOP_PAD + WALL_SIZE // 2 + 1
    for row in array:
        x = BORDER_WIDTH + WALL_SIZE // 2 + 1
        for point in row:
            if point:
                walls.append(Wall((x, y)))
            x += WALL_SIZE
        y += WALL_SIZE
    return walls


def build_borders(screen):
    borders = []
    x = 0
    while x < SCREEN_WIDTH:
        borders.append(
            pygame.draw.rect(
                screen,
                WHITE,
                pygame.Rect(x, 0, BORDER_WIDTH, BORDER_WIDTH + TOP_PAD)
            ),
        )
        borders.append(
            pygame.draw.rect(
                screen,
                WHITE,
                pygame.Rect(x, SCREEN_HEIGHT - BORDER_WIDTH,
                            BORDER_WIDTH, BORDER_WIDTH)
            )
        )
        x += BORDER_WIDTH
    y = TOP_PAD
    while y < SCREEN_HEIGHT:
        borders.append(
            pygame.draw.rect(
                screen,
                WHITE,
                pygame.Rect(0, y, BORDER_WIDTH, BORDER_WIDTH)
            )
        )
        borders.append(
            pygame.draw.rect(
                screen,
                WHITE,
                pygame.Rect(SCREEN_WIDTH - BORDER_WIDTH, y,
                            BORDER_WIDTH, BORDER_WIDTH)
            )
        )
        y += BORDER_WIDTH
    return borders


def build_walls(map_walls):
    walls = pygame.sprite.Group()
    for wall in map_walls:
        walls.add(wall)
    return walls


def testmap(X=1):
    '''
    Resolution
    25x18 blocks
    '''
    map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],

    ]
    return array_to_walls(map)


def testmap2(X=1):
    '''
    Resolution
    25x18 blocks
    '''
    map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X,],
        [0, 0, X, 0, 0, 0, 0, 0, X, X, X, X, 0, 0, X, 0, 0, 0, 0, X, 0, 0, 0, 0, X,],
        [0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, X,],
        [0, 0, X, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, X, 0, 0, 0, 0, X, 0, 0, 0, 0, X,],
        [0, 0, X, X, X, X, X, X, 0, 0, X, 0, 0, 0, 0, 0, 0, X, 0, X, 0, 0, 0, 0, X,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, X,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0,],
        [X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X,],
        [0, 0, X, 0, 0, 0, 0, 0, X, X, X, X, 0, 0, X, 0, 0, 0, 0, X, 0, 0, 0, 0, X,],
        [0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, X,],
        [0, 0, X, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, X, 0, 0, 0, 0, X, 0, 0, 0, 0, X,],
        [0, 0, X, X, X, X, X, X, 0, 0, X, 0, 0, 0, 0, 0, 0, X, 0, X, 0, 0, 0, 0, X,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, X,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0,],
        [X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],

    ]
    return array_to_walls(map)
