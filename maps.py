import pygame
from constants import *  # noqa:F403 flake8 ignore
# import debug_me
'''
map builders
Linting is ignored in this file for "Line is too long"
'''


def test():
    # 25x18 map
    return (
        '#########################'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#               #       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#                       #'
        '#########################'
    )


def level_1():
    # 25x18 map
    return (
        '#########################'
        '#                       #'
        '#   ######    ##        #'
        '#          #   #        #'
        '#          #   #        #'
        '####   #####       ######'
        '#                       #'
        '#                       #'
        '#   #####          #    #'
        '#                  ##   #'
        '#      #            #   #'
        '#      #            #   #'
        '#      #     #####  #   #'
        '#      #                #'
        '#      ######    #####  #'
        '#   ####       #        #'
        '#              #        #'
        '#########################'
    )


class Map:
    def __init__(self, map_name=test):
        self.map = map_name()

    def blit_walls(self, screen):
        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                if self.map[row * MAP_WIDTH + col] == '#':
                    pygame.draw.rect(
                        screen,
                        RED,
                        (
                            col * WALL_SIZE,
                            row * WALL_SIZE,
                            WALL_SIZE, WALL_SIZE,
                        )
                    )
                    # font = pygame.font.SysFont("Arial", 10)
                    # debug_me.print_square(screen, row, col, font)

    def map_check(self, mapcheck):
        map_x = mapcheck[0] // WALL_SIZE
        map_y = mapcheck[1] // WALL_SIZE
        if (map_x >= 0 and map_x < MAP_WIDTH and
           map_y >= 0 and map_y < MAP_HEIGHT):
            map_tile = map_y * MAP_WIDTH + map_x
            if self.map[int(map_tile)] == '#':
                return True
        return False
