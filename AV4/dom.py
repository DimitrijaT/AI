from searching_framework.utils import Problem
from searching_framework.informed_search import *
from searching_framework.uninformed_search import *


def get_x_and_y_only(state):
    return []


def move_left(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 > 0 and [x1 - 1, y1] not in obstacles and [x1 - 1, y1] != [x2, y2] and [x1 - 1, y1] != [x3, y3]:
        x1 -= 1
    return x1


def move_up(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 < 6 and [x1, y1 + 1] not in obstacles and [x1, y1 + 1] != [x2, y2] and [x1, y1 + 1] != [x3, y3]:
        y1 += 1
    return y1


def move_down(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 > 0 and [x1, y1 - 1] not in obstacles and [x1, y1 - 1] != [x2, y2] and [x1, y1 - 1] != [x3, y3]:
        y1 -= 1
    return y1


class Molecule(Problem):
    def __init__(self, obstacles_list, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles_list
        self.N = 4
        self.M = 5

    def successor(self, state):
        # (h1_x,h1_y,o1_x,o1_y,h2_x,h2_y)
        successors = dict()

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] + 1 == state[4]

    @staticmethod
    def check_valid(new_x, new_y, state, obstacles, n, m):
        # ((((x1, y1), d1), ((x2, y2), d2), … ,((xk, yk), dk)), (xG, yG))
        pacman_children = get_x_and_y_only(state)  # ((x1, y1),(x2, y2), … , (xk, yk))
        ghost_x = state[1][0]  # xG
        ghost_y = state[1][1]  # yG
        if (new_x, new_y) not in obstacles and \
                n > new_x >= 0 and \
                m > new_y >= 0 and \
                (new_x, new_y) != (ghost_x, ghost_y) and \
                (new_x, new_y) not in pacman_children:
            return True
        else:
            return False


def h(self, node):
    state = node.state
    h1_x, h1_y = state[0], state[1]
    o_x, o_y = state[2], state[3]
    h2_x, h2_y = state[4], state[5]

    value = 0

    if h1_y != o_y:
        if h1_x == (o_x - 1):
            value += 1
        else:
            value += 2
    else:
        if h1_x > o_x:
            value += 3
        elif h1_x < (o_x - 1):
            value += 1

    if h2_y != o_y:
        if h2_x == (o_x + 1):
            value += 1
        else:
            value += 2
    else:
        if h2_x > o_x:
            value += 3
        elif h2_x < (o_x + 1):
            value += 1

    if h1_x == h2_x and h1_y != o_y:
        value -= 1

    return value


if __name__ == '__main__':
    # [x,y],[x,y]...
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = Molecule(obstacles_list, (h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1]), )

    result = astar_search(molecule)
    print(result.solution())

    result2 = breadth_first_graph_search(molecule)
    print(result2.solution())
