from constraint import *

if __name__ == '__main__':
    solverName = input()
    if solverName == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    elif solverName == "MinConflictsSolver":
        problem = Problem(MinConflictsSolver())
    else:
        problem = Problem()  # BacktrackingSolver

    board_size = 9
    variables = [(i, j) for i in range(9) for j in range(9)]
    domain = range(1, 10)
    problem.addVariables(variables, domain)

    for x in range(board_size):
        row = []
        column = []
        for y in range(board_size):
            row.append((x, y))
            column.append((y, x))
        # print(column)
        problem.addConstraint(AllDifferentConstraint(), tuple(row))
        problem.addConstraint(AllDifferentConstraint(), tuple(column))

    for r in range(0, 9, 3):
        for z in range(0, 9, 3):
            block = []
            for x in range(3):
                for y in range(3):
                    block.append((y + r, x + z))
            # print(block)
            problem.addConstraint(AllDifferentConstraint(), tuple(block))

    print(problem.getSolution())
