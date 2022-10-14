from constraint import *


def diagonals(queen):
    diagonals = []
    for i in range(0, N):
        if queen[0] - i >= 0 and queen[1] + i < N:
            diagonals.append((queen[0] - i, queen[1] + i))
        if queen[0] + i < N and queen[1] - i >= 0:
            diagonals.append((queen[0] + i, queen[1] - i))
        if queen[0] - i >= 0 and queen[1] - i >= 0:
            diagonals.append((queen[0] - i, queen[1] - i))
        if queen[0] + i < N and queen[1] + i < N:
            diagonals.append((queen[0] + i, queen[1] + i))
    return diagonals


def not_attacking(queen1, queen2):
    if queen1[0] != queen2[0] and queen1[1] != queen2[1] and queen2 not in diagonals(queen1):
        return True
    else:
        return False


global N

if __name__ == '__main__':

    problem = Problem()
    N = int(input())

    domain = [(i, j) for i in range(0, N) for j in range(0, N)]

    # print(domain)

    queens = range(1, N + 1)

    problem.addVariables(queens, domain)

    for queen1 in queens:
        for queen2 in queens:
            if queen1 < queen2:
                problem.addConstraint(not_attacking, (queen1, queen2))

    if (N <= 6):
        print(problem.getSolutions())
    else:
        print(problem.getSolution())
