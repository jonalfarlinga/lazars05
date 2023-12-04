import math
from constants import *  # noqa:F403 flake8 ignore
from pygame.draw import line


# converts a heading to a unit vector
def deg_to_vector(deg):
    unit_vector = (
        math.cos((deg * math.pi) / 180),
        math.sin((deg * math.pi) / 180)
    )
    return unit_vector


# radian to vector
def rad_to_vector(rad):
    unit_vector = (
        math.cos(rad),
        math.sin(rad)
    )
    return unit_vector


# measures and returns the distance between two coordinates
def distance(point1, point2):
    distance = math.sqrt(
        (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    )
    return distance


# takes a point and radian direction and an new coord component,
# if terms_of_x returns y2
# else returns x2
def param_eq(source, new, rad, terms_of_x=True):
    x1, y1 = source
    if terms_of_x:
        return y1 + ((new - x1) * math.sin(rad) / math.cos(rad))
    else:
        return x1 + ((new - y1) * math.cos(rad) / math.sin(rad))


# takes a point and vector and an x2, returns y2
def linear_eq(source, x2, unit_vector):
    x1, y1 = source
    uvx, uvy = unit_vector
    return y1 + ((x2 - x1) / uvx * uvy)


# takes a point and vector and a y2, returns x2
def linear_eq_inv(source, y2, unit_vector):
    x1, y1 = source
    uvx, uvy = unit_vector
    return x1 + ((y2 - y1) / uvy * uvx)


# rounds up for decimals 0.5 and above, or rounds down
def proper_round(num):
    test = num * 10
    if test % 10 >= 5:
        return math.ceil(num)
    else:
        return math.floor(num)


# takes x/y vector components, the previous key value, and a rect
# returns a reflected vector
def reflect_direction(uvx, uvy, last, rect, terms_of_x):
    if terms_of_x:
        if rect.left < last < rect.right:
            uvy = -uvy
        else:
            uvx = -uvx
    else:
        if rect.top < last < rect.bottom:
            uvx = -uvx
        else:
            uvy = -uvy
    return uvx, uvy


# assumes all collision rects are square.
def find_bounce(source, rad, rects, ray):
    if rad < PI:
        refrad = rad + PI
    else:
        refrad = rad - PI
    collide_list = ray.collidelistall(rects)
    if PI * 1.25 < refrad <= PI * 1.75:  # 5pi/4 to 7pi/4 - horizontal wall
        stop = 0
        for index in collide_list:
            rect = rects[index]
            if rect.bottom > stop:
                stop = rect.bottom
        y2 = stop
        x2 = source[0] + (
            (stop - source[1]) * math.cos(rad) / math.sin(rad)
        )
        # if rad < PI:
        #    rad = PI2 - PI - rad
        # else:
        rad = -PI - rad
    elif PI * .75 < refrad <= PI * 1.25:  # 3pi/4 to 5pi/4 - vertical wall
        stop = SCREEN_WIDTH
        for index in collide_list:
            rect = rects[index]
            if rect.left < stop:
                stop = rect.left
        x2 = stop
        y2 = source[1] + (
            (stop - source[0]) * math.sin(rad) / math.cos(rad)
        )
        # if rad < PI:
        #    rad = PI - rad
        # else:
        rad = -rad
    elif PI / 4 < refrad <= PI * .75:  # pi/4 to 3pi/4 - horizontal wall
        stop = SCREEN_HEIGHT
        for index in collide_list:
            rect = rects[index]
            if rect.top < stop:
                stop = rect.top
        y2 = stop
        x2 = source[0] + (
            (stop - source[1]) * math.cos(rad) / math.sin(rad)
        )
        # if rad < PI:
        #    rad = PI2 + PI - rad
        # else:
        rad = -PI - rad
    else:   # remaimder is < pi/4 or > 7pi/4 - vertical wall
        stop = 0
        for index in collide_list:
            rect = rects[index]
            if rect.right > stop:
                stop = rect.right
        x2 = stop
        y2 = source[1] + (
            (stop - source[0]) * math.sin(rad) / math.cos(rad)
        )
        # if rad < PI:
        #    rad = PI2 + PI - rad
        # else:
        rad = -rad
    while rad > PI2 or rad < 0:
        if rad < 0:
            rad += PI2
        elif rad > PI2:
            rad -= PI2
    return x2, y2, rad


# given a point, bearing and list of rects
# finds the line and 4 reflections, and returns a list of point pairs.
def calculate_line(source, rad, screen, rects, bounces):
    # while source and bounces less than bounces
    #   draw a line from source to SCREEN_EDGE <-- SCREEN_EDGE is based on quad
    #       find all collisions with rects
    # noqa      find rect according to rect.edge closest to player
    # noqa      calculate x2 or y2 by player angle and rect.edge
    #           calculate reflected angle
    #           --> find_bounce
    #   append bounce
    #   source = bounce
    bounce_points = []

    while source and len(bounce_points) < bounces:
        if PI / 4 < rad <= PI * .75:       # pi/4 to 3pi/4
            wally = SCREEN_HEIGHT
            wallx = source[0] + (
                (SCREEN_HEIGHT - source[1]) * math.cos(rad) / math.sin(rad)
            )
        elif PI * .75 < rad <= PI * 1.25:  # 3pi/4 to 5pi/4
            wallx = 0
            wally = source[1] + (
                (0 - source[0]) * math.sin(rad) / math.cos(rad)
            )
        elif PI * 1.25 < rad <= PI * 1.75:  # 5pi/4 to 7pi/4
            wally = 0
            wallx = source[0] + (
                (0 - source[1]) * math.cos(rad) / math.sin(rad)
            )
        else:               # remainder is < p/4 or > 7pi/4
            wallx = SCREEN_WIDTH
            wally = source[1] + (
                (SCREEN_WIDTH - source[0]) * math.sin(rad) / math.cos(rad)
            )
        ray = line(
            screen,
            NONE_COLOR,
            source,
            (wallx, wally),
        )
        x2, y2, rad = find_bounce(source, rad, rects, ray)
        bounce_points.append((x2, y2))
        source = (x2, y2)
    return bounce_points
