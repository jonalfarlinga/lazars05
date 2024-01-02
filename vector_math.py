from math import sqrt, sin, cos, pi, floor
from constants import *  # noqa:F403


def deg_to_vector(deg):
    return (
        cos(deg * pi / 180),
        sin(deg * pi / 180),
    )


# measures and returns the distance between two coordinates
def distance(point1, point2):
    distance = sqrt(
        (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    )
    return distance


def raycast_DDA(source, deg, game_map):
    uvx, uvy = deg_to_vector(deg)
    source = source[0] / WALL_SIZE, source[1] / WALL_SIZE

    # meaure Step Size
    try:
        vx_stepsize = abs(1 / uvx)
    except ZeroDivisionError:
        vx_stepsize = float('inf')
    try:
        vy_stepsize = abs(1 / uvy)
    except ZeroDivisionError:
        vy_stepsize = float('inf')

    # establish starting condition
    vMapCheck = source
    if uvx < 0:
        vStepx = -1
        vRayLength1Dx = (source[0] - vMapCheck[0]) * vx_stepsize
    else:
        vStepx = 1
        vRayLength1Dx = (vMapCheck[0] + 1 - source[0]) * vx_stepsize
    if uvy < 0:
        vStepy = -1
        vRayLength1Dy = (source[1] - vMapCheck[1]) * vy_stepsize
    else:
        vStepy = 1
        vRayLength1Dy = (vMapCheck[1] + 1 - source[1]) * vy_stepsize

    # perform walk until collision or range check
    bTileFound = False
    fMaxDistance = SCREEN_WIDTH / WALL_SIZE
    fDistance = 0
    while not bTileFound and fDistance < fMaxDistance:
        # walk along shortest path
        if vRayLength1Dx < vRayLength1Dy:
            vMapCheck = (vMapCheck[0] + vStepx, vMapCheck[1])
            fDistance = vRayLength1Dx
            vRayLength1Dx += vx_stepsize
        else:
            vMapCheck = (vMapCheck[0], vMapCheck[1] + vStepy)
            fDistance = vRayLength1Dy
            vRayLength1Dy += vy_stepsize

        # test tile at new test point
        bTileFound = game_map.map_check(vMapCheck)

    return (floor(vMapCheck[0] * WALL_SIZE), floor(vMapCheck[1]) * WALL_SIZE), deg


"""
    if bTileFound:

        test1 = (vMapCheck[0], vMapCheck[1])
        test2 = (vMapCheck[0], vMapCheck[1])
        # if 45 <= deg < 135:
            # block1 = (last_block[0] + 1,
            #          last_block[1])
            # block2 = (last_block[0] - 1,
            #          last_block[1])
            # if game_map.map_check(block1) or game_map.map_check(block2):
        if game_map.map_check(test1) or game_map.map_check(test2):
            incident = 0 - deg
        else:
            incident = 90 - deg
        '''
                normal = 90
            else:
                normal = 360
        elif 225 <= deg < 315:
            if block1[0] < block2[0]:
                normal = 360
            else:
                normal = 90
        elif 135 <= deg < 225:
            if block1[1] < block2[1]:  # BROKEN
                normal = 360
            else:
                normal = 90
        else:
            if block1[1] > block2[1]:
                normal = 360
            else:
                normal = 90

        '''
        deg = deg - 2 * incident
        # if deg < 0:
        #    deg += 360
        # elif deg > 360:
        #    deg -= 360

        return (
            (source[0] + uvx * fDistance,
             source[1] + uvy * fDistance),
            deg
        )
    else:
        return (0, 0), deg
"""


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
