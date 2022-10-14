if __name__ == '__main__':

    N = int(input())
    M = int(input())

    matrix = []

    # for i in range(N):
    #     podlist = []
    #     for j in range(M):
    #         podlist.append(int(input()))
    #     list.append(podlist)

    for i in range(0,N):
        podlist = [int(element) for element in input().split(" ")]
        matrix.append(podlist)

    print(matrix)

    # matrix = [(x * 2, y * 2, z * 2) for (x, y, z) in list]

    # list = [element * 2 for row in matrix for element in row]

    matrix = [[element * 2 for element in row] for row in matrix]

    variant2 = [[matrix[i][j] * 2 for j in range(M)] for i in range(N)]

    print(matrix)
    print(variant2)
