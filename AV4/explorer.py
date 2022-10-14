from searching_framework.utils import Problem
from searching_framework.informed_search import *


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):
        # d = -1 (down)
        # d = 1  (up)
        # (x,y, (x_o1 ,y_o1, d_o1), (x_o2, y_o2, d_o2))

        successor = dict()

        man_x = state[0]
        man_y = state[1]

        obstacle1 = list(state[2])
        obstacle2 = list(state[3])

        if obstacle1[2] == 1:
            if obstacle1[1] == self.grid_size[1] - 1:
                obstacle1[2] = -1
                obstacle1[1] -= 1
            else:
                obstacle1[1] += 1
        else:
            if obstacle1[1] == 0:
                obstacle1[2] = 1
                obstacle1[1] += 1
            else:
                obstacle1[1] -= 1

        if obstacle2[2] == 1:
            if obstacle2[1] == self.grid_size[1] - 1:
                obstacle2[2] = -1
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else:
            if obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        obstacles = [(obstacle1[0], obstacle1[1]), (obstacle2[0], obstacle2[1])]

        # (x,y, (x_o1 ,y_o1, d_o1), (x_o2, y_o2, d_o2))

        # right
        if man_x + 1 < self.grid_size[0] and (man_x + 1, man_y) not in obstacles:
            successor["Chovecheto odi desno"] = (
                man_x + 1, man_y, (obstacle1[0], obstacle1[1], obstacle1[2]),
                (obstacle2[0], obstacle2[1], obstacle2[2]))

        if man_x - 1 >= 0 and (man_x - 1, man_y) not in obstacles:
            successor["Chovecheto odi levo"] = (
                man_x - 1, man_y, (obstacle1[0], obstacle1[1], obstacle1[2]),
                (obstacle2[0], obstacle2[1], obstacle2[2]))

        if man_y + 1 < self.grid_size[1] and (man_x, man_y + 1) not in obstacles:
            successor["Chovecheto odi gore"] = (
                man_x, man_y + 1, (obstacle1[0], obstacle1[1], obstacle1[2]),
                (obstacle2[0], obstacle2[1], obstacle2[2]))

        if man_y - 1 >= 0 and (man_x, man_y - 1) not in obstacles:
            successor["Chovecheto odi dolu"] = (
                man_x, man_y - 1, (obstacle1[0], obstacle1[1], obstacle1[2]),
                (obstacle2[0], obstacle2[1], obstacle2[2]))

        return successor

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # (x,y, (x_o1 ,y_o1, d_o1), (x_o2, y_o2, d_o2))

        # (g0, g1)
        return (state[0], state[1]) == self.goal

    def h(self, node):
        x_man = node.state[0]
        y_man = node.state[1]
        x_house = self.goal[0]
        y_house = self.goal[1]
        return abs(x_man - x_house) + abs(y_man - y_house)


if __name__ == '__main__':
    goal_state = (7, 4)
    init_state = (0, 2)
    obstacle1 = (2, 5, -1)
    obstacle2 = (5, 0, 1)

    explorer = Explorer((init_state[0], init_state[1], obstacle1, obstacle2), goal_state)

    answer = astar_search(explorer)

    print(answer.solution())