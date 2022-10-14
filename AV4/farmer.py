from searching_framework.utils import Problem
from searching_framework.informed_search import *


def valid(state):
    farmer, volk, jare, zelka = state
    if farmer != volk and volk == jare:
        return False
    if farmer != jare and jare == zelka:
        return False
    return True


class Farmer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        # (farmer, volk, jare, zelka) (w,e,w,e)
        successors = dict()
        farmer, volk, jare, zelka = state[0], state[1], state[2], state[3]

        # Farmer se prenesuva sebesi
        farmer_new = "e" if farmer == "w" else "w"
        state_new = farmer_new, volk, jare, zelka
        if valid(state_new):
            successors["Farmer_nosi_farmer"] = state_new

        if farmer == volk:
            volk_new = "e" if farmer == "w" else "w"
            state_new = volk_new, volk_new, jare, zelka
            if valid(state_new):
                successors["Farmer_nosi_volk"] = state_new

        if farmer == jare:
            jare_new = "e" if farmer == "w" else "w"
            state_new = jare_new, volk, jare_new, zelka
            if valid(state_new):
                successors["Farmer_nosi_jare"] = state_new

        if farmer == zelka:
            zelka_new = "e" if farmer == "w" else "w"
            state_new = zelka_new, volk, jare, zelka_new
            if valid(state_new):
                successors["Farmer_nosi_zelka"] = state_new

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        counter = 0
        for x, y in zip(state, self.goal):
            if x != y:
                counter += 1

        return counter


if __name__ == '__main__':
    initial_state = ("e", "e", "e", "e")
    goal_state = ("w", "w", "w", "w")
    farmer = Farmer(initial_state, goal_state)
    result = astar_search(farmer)
    print(result.solution())
