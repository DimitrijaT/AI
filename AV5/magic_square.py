from constraint import *

if __name__ == '__main__':
    problem = Problem()
    variables = range(0, 16)  # 0 - 15
    domain = range(1, 17)  # 1 - 16

    problem.addVariables(variables, domain)

    problem.addConstraint(AllDifferentConstraint(), variables)
    """
    0  1  2  3
    4  5  6  7
    8  9  10 11
    12 13 14 15
    """
    # for row in range(0, 4):
    #     print([row * 4 + i for i in range(0, 4)])
    #
    # print()
    # for column in range(0, 4):
    #     print([column + 4 * i for i in range(0, 4)])

    for row in range(0, 4):
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(0, 4)])

    for column in range(0, 4):  # col = 0 -> [0+4*0, 0+4*1, 0+4*2, 0+4*3] = [0,4,8,12]
        problem.addConstraint(ExactSumConstraint(34), [column + 4 * i for i in range(0, 4)])

    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))

    # problem.addConstraint(ExactSumConstraint(34), range(12, 0, -3))

    # for i in range(12, 0, -3):
    #     print(i)
    # 12, 9, 6, 3

    solution = problem.getSolution()

    print(solution)
