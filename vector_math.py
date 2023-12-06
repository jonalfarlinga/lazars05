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
    if uvx == 0:
        uvx = 0.000001
    if uvy == 0:
        uvy = 0.000001
    vx_stepsize = abs(1 / uvx)
    vy_stepsize = abs(1 / uvy)
    vMapCheck = source
    if uvx < 0:
        vStepx = -1
        vRayLength1Dx = (source[0] - floor(vMapCheck[0])) * vx_stepsize
    else:
        vStepx = 1
        vRayLength1Dx = (floor(vMapCheck[0] + 1) - source[0]) * vx_stepsize
    if uvy < 0:
        vStepy = -1
        vRayLength1Dy = (source[1] - floor(vMapCheck[0])) * vy_stepsize
    else:
        vStepy = 1
        vRayLength1Dy = (floor(vMapCheck[1] + 1) - source[1]) * vy_stepsize

    bTileFound = False
    fMaxDistance = SCREEN_WIDTH
    fDistance = 0

    while not bTileFound and fDistance < fMaxDistance:
        if vRayLength1Dx < vRayLength1Dy:
            vMapCheck = (vMapCheck[0] + vStepx, vMapCheck[1])
            fDistance = vRayLength1Dx
            vRayLength1Dx += vx_stepsize
        else:
            vMapCheck = (vMapCheck[0], vMapCheck[1] + vStepy)
            fDistance = vRayLength1Dy
            vRayLength1Dy += vy_stepsize

        if (vMapCheck[0] >= 0 and vMapCheck[0] < MAP_WIDTH and
           vMapCheck[1] >= 0 and vMapCheck[1] < MAP_HEIGHT):
            if game_map.map[vMapCheck[1] * MAP_WIDTH + vMapCheck[0]] == '#':
                bTileFound = True

        if bTileFound:
            return (
                source[0] + uvx * fDistance,
                source[1] + uvy * fDistance,
            )
        else:
            if uvx > 0.707:
                return (
                    SCREEN_WIDTH, linear_eq(source, SCREEN_WIDTH, (uvx, uvy))
                )
            elif uvy > 0.707:
                return (
                    SCREEN_HEIGHT, linear_eq_inv(
                        source,
                        SCREEN_HEIGHT,
                        (uvx, uvy)
                    )
                )
            elif uvx < 0.707:
                return (
                    0, linear_eq(source, 0, (uvx, uvy))
                )
            elif uvy < 0.707:
                return (
                    0, linear_eq_inv(source, 0, (uvx, uvy))
                )


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
