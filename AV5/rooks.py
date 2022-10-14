from constraint import *


# (i1,j1), (i2,j2)
def not_attacking(rook1, rook2):
    return rook1[0] != rook2[0] and rook1[1] != rook2[1]


if __name__ == '__main__':
    problem = Problem()
    # domain = []
    # for i in range(0, 8):
    #     for j in range(0, 8):
    #         domain.append((i, j))
    domain = [(i, j) for i in range(0, 8) for j in range(0, 8)]  # domain

    rooks = range(1, 9)  # variables

    problem.addVariables(rooks, domain)

    for rook1 in rooks:
        for rook2 in rooks:
            # print("ROOK1 " + str(rook1))
            # print("ROOK2 " + str(rook2))
            # if (rook1 != rook2):
            if rook1 < rook2:  # OPTIMIZACIJA NA PRETHODNOTO
                problem.addConstraint(not_attacking, (rook1, rook2))

    solution = problem.getSolution()
    print(solution)
