from constraint import *


def knights_not_attacking(knight1, knight2):
    return abs(knight1[0] - knight2[0]) != abs(knight1[1] - knight2[1])


if __name__ == '__main__':
    problem = Problem()
    domain = [(i, j) for i in range(0, 8) for j in range(0, 8)]
    variables = range(1, 9)
    problem.addVariables(variables, domain)

    for knight1 in variables:
        for knight2 in variables:
            if knight1 < knight2:
                problem.addConstraint(knights_not_attacking, (knight1, knight2))

    solution = problem.getSolution()

    print(solution)
