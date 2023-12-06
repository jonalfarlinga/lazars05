import pygame
import os
from constants import *  # noqa:F403 flake8 ignore
# import debug_me
'''
map builders
Linting is ignored in this file for "Line is too long"
'''


def test():
    global MAP_HEIGHT
    MAP_HEIGHT = 18
    global MAP_WIDTH
    MAP_WIDTH = 25
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
    global MAP_HEIGHT
    MAP_HEIGHT = 18
    global MAP_WIDTH
    MAP_WIDTH = 25
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
