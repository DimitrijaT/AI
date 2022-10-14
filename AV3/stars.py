"""
• K1 - за придвижување од тип 1 (горе + лево)
• K2 - за придвижување од тип 2 (горе + десно)
• K3 - за придвижување од тип 3 (десно + горе)
• K4 - за придвижување од тип 4 (десно + долу)
• K5 - за придвижување од тип 5 (долу + десно)
• K6 - за придвижување од тип 6 (долу + лево)
• K7 - за придвижување од тип 7 (лево + долу)
• K8 - за придвижување од тип 8 (лево + горе)
"""

"""
B1 - за придвижување од тип 1 (движење за едно поле во насока
горе-лево)
• B2 - за придвижување од тип 2 (движење за едно поле во насока
горе-десно)
• B3 - за придвижување од тип 3 (движење за едно поле во насока
долу-лево)
• B4 - за придвижување од тип 4 (движење за едно поле во насока
долу-десно)
"""

from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def k1(kx, ky, lx, ly):  # up up left
    if 0 <= kx - 1 < 8 and 0 <= ky + 2 < 8 and [kx - 1, ky + 2] != [lx, ly]:
        kx -= 1
        ky += 2
    return kx, ky


def k2(kx, ky, lx, ly):  # up up right
    if 0 <= kx + 1 < 8 and 0 <= ky + 2 < 8 and [kx + 1, ky + 2] != [lx, ly]:
        kx += 1
        ky += 2
    return kx, ky


def k3(kx, ky, lx, ly):  # right right up
    if 0 <= kx + 2 < 8 and 0 <= ky + 1 < 8 and [kx + 2, ky + 1] != [lx, ly]:
        kx += 2
        ky += 1
    return kx, ky


def k4(kx, ky, lx, ly):  # right right down
    if 0 <= kx + 2 < 8 and 0 <= ky - 1 < 8 and [kx + 2, ky - 1] != [lx, ly]:
        kx += 2
        ky -= 1
    return kx, ky


def k5(kx, ky, lx, ly):  # down down right
    if 0 <= kx + 1 < 8 and 0 <= ky - 2 < 8 and [kx + 1, ky - 2] != [lx, ly]:
        kx += 1
        ky -= 2
    return kx, ky


def k6(kx, ky, lx, ly):  # down down left
    if 0 <= kx - 1 < 8 and 0 <= ky - 2 < 8 and [kx - 1, ky - 2] != [lx, ly]:
        kx -= 1
        ky -= 2
    return kx, ky


def k7(kx, ky, lx, ly):  # left left down
    if 0 <= kx - 2 < 8 and 0 <= ky - 1 < 8 and [kx - 2, ky - 1] != [lx, ly]:
        kx -= 2
        ky -= 1
    return kx, ky


def k8(kx, ky, lx, ly):  # left left up
    if 0 <= kx - 2 < 8 and 0 <= ky + 1 < 8 and [kx - 2, ky + 1] != [lx, ly]:
        kx -= 2
        ky += 1
    return kx, ky


def b1(lx, ly, kx, ky):  # горе-лево
    if 0 <= lx - 1 < 8 and 0 <= ly + 1 < 8 and [lx - 1, ly + 1] != [kx, ky]:
        lx -= 1
        ly += 1
    return lx, ly


def b2(lx, ly, kx, ky):  # горе-десно
    if 0 <= lx + 1 < 8 and 0 <= ly + 1 < 8 and [lx + 1, ly + 1] != [kx, ky]:
        lx += 1
        ly += 1
    return lx, ly


def b3(lx, ly, kx, ky):  # долу-лево
    if 0 <= lx - 1 < 8 and 0 <= ly - 1 < 8 and [lx - 1, ly - 1] != [kx, ky]:
        lx -= 1
        ly -= 1
    return lx, ly


def b4(lx, ly, kx, ky):  # долу-десно
    if 0 <= lx + 1 < 8 and 0 <= ly - 1 < 8 and [lx + 1, ly - 1] != [kx, ky]:
        lx += 1
        ly -= 1
    return lx, ly


class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        # (kx, ky, lx, ly, ((star1x, star1y), (star2x, star2y)... (starNx, starNy)))

        successor = dict()

        knight_x = state[0]
        knight_y = state[1]

        bishop_x = state[2]
        bishop_y = state[3]

        star_pos = state[4]

        new_x, new_y = k1(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successor["K1"] = (new_x, new_y, bishop_x, bishop_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))
        new_x, new_y = k2(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successor["K2"] = (new_x, new_y, bishop_x, bishop_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))
        new_x, new_y = k3(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successor["K3"] = (new_x, new_y, bishop_x, bishop_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))
        new_x, new_y = k4(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successor["K4"] = (new_x, new_y, bishop_x, bishop_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))
        new_x, new_y = k5(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successor["K5"] = (new_x, new_y, bishop_x, bishop_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))
        new_x, new_y = k6(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successor["K6"] = (new_x, new_y, bishop_x, bishop_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))
        new_x, new_y = k7(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successor["K7"] = (new_x, new_y, bishop_x, bishop_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))
        new_x, new_y = k8(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successor["K8"] = (new_x, new_y, bishop_x, bishop_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))
        # BISHOP
        new_x, new_y = b1(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [new_x, new_y]:
            successor["B1"] = (knight_x, knight_y, new_x, new_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))

        new_x, new_y = b2(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [new_x, new_y]:
            successor["B2"] = (knight_x, knight_y, new_x, new_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))

        new_x, new_y = b3(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [new_x, new_y]:
            successor["B3"] = (knight_x, knight_y, new_x, new_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))

        new_x, new_y = b4(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [new_x, new_y]:
            successor["B4"] = (knight_x, knight_y, new_x, new_y,
                               tuple([star for star in star_pos if (star[0], star[1]) != (new_x, new_y)]))

        return successor

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[4]) == 0


if __name__ == '__main__':
    knight = [2, 5]
    bishop = [5, 1]
    stars = ((1, 1), (4, 3), (6, 6))
    stars = Stars((knight[0], knight[1], bishop[0], bishop[1], stars))
    result = breadth_first_graph_search(stars)
    print(result.solution())
