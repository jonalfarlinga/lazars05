import math
from maps import collide_point
from constants import *  # noqa:F403 flake8 ignore


# converts a heading to a unit vector
def deg_to_vector(deg):
    unit_vector = (
        math.cos((deg * math.pi) / 180),
        math.sin((deg * math.pi) / 180)
    )
    return unit_vector


# measures and returns the distance between two coordinates
def distance(point1, point2):
    distance = math.sqrt(
        (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    )
    return distance


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
def proper_round(num, dig=0):
    exp = 10 ** dig
    test = num * exp * 10
    if test % 10 >= 5:
        return math.ceil(num * exp) / exp
    else:
        return math.floor(num * exp) / exp


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


# takes x/y vector components, the previous key value, and a rect
# returns a reflected vector
def reflect(uvx, uvy, collision):
    if collision == "horizontal":
        uvy = -uvy
    else:
        uvx = -uvx
    return uvx, uvy


# draw a ray from the player to the first block
def calculate_line(source, deg, map, bounces):
    bounce_points = []
    uvx, uvy = deg_to_vector(deg)

    while source and len(bounce_points) < bounces:
        for depth in range(SCREEN_WIDTH):
            point = (source[0] + uvx * depth,
                     source[1] + uvy * depth)
            collision = collide_point(point, map)
            if collision:
                bounce_points.append(point)
                uvx, uvy = reflect(uvx, uvy, collision)
                break
        source = point
    return bounce_points
