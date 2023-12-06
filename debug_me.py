import pygame
from constants import *  # noqa:F403 flake8 ignore


def debug(mouse_pos, screen):
    font = pygame.font.SysFont("Arial", 20)
    track = font.render(str(mouse_pos), True, (255, 255, 255))
    screen.blit(track, (SCREEN_WIDTH - 100, 10))
    """
    for block in blocks:
        if hasattr(block, "blit_sprite"):
            block.blit_sprite(screen)
            if block.rect.collidepoint(mouse_pos):
                print("COLLISION" + str(block))
        elif block.collidepoint(mouse_pos):
            print("COLLISION" + str(block)) """


# Show FPS
def fps_counter(clock, screen, font):
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps, 1, YELLOW)
    screen.blit(fps_t, (10, 10))


def print_square(screen, row, col, font):
    coord = font.render(f"{str(col)},{str(row)}", 1, YELLOW)
    screen.blit(coord, (col * WALL_SIZE, row * WALL_SIZE))
