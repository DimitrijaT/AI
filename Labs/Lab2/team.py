from constraint import *


def all_diff(m1, m2):
    if m1[1] != m2[1] and m1[0] != m2[0]:
        return True
    else:
        return False


def max_sum(m1, m2, m3, m4, m5, tl6):
    if (m1[0] + m2[0] + m3[0] + m4[0] + m5[0] + tl6[0]) <= 100.0:
        return True
    else:
        return False


if __name__ == '__main__':
    N1 = int(input())
    member_list = []
    for i in range(N1):
        # 31.3 A
        member = input().split(" ")
        member_list.append((float(member[0]), member[1]))

    N2 = int(input())
    teamleader_list = []
    for i in range(N2):
        # 31.3 A
        leader = input().split(" ")
        teamleader_list.append((float(leader[0]), leader[1]))

    # print(member_list)
    # print(teamleader_list)

    problem = Problem()

    variables = range(1, 6)
    problem.addVariables(variables, member_list)
    problem.addVariable(6, teamleader_list)

    for person1 in variables:
        for person2 in variables:
            if person1 < person2:
                problem.addConstraint(all_diff, (person1, person2))

    problem.addConstraint(max_sum, (1, 2, 3, 4, 5, 6))

    solutions = problem.getSolutions()
    max_result = None
    max_weight = -1
    for solution in solutions:
        calculated_weight = solution[1][0] + solution[2][0] + solution[3][0] + solution[4][0] + solution[5][0] + \
                            solution[6][0]
        if calculated_weight > max_weight:
            max_weight = calculated_weight
            max_result = solution

    # print(max_result)
    # print(max_weight)
    print(f'Total score: {max_weight}')
    print(f'Team leader: {max_result[6][1]}')
    print(f'Participant 1: {max_result[1][1]}')
    print(f'Participant 2: {max_result[2][1]}')
    print(f'Participant 3: {max_result[3][1]}')
    print(f'Participant 4: {max_result[4][1]}')
    print(f'Participant 5: {max_result[5][1]}')
