def multiply(element, i, N):
    if i < N / 2:
        return element * 2
    else:
        return element * 3


if __name__ == '__main__':

    N = int(input())
    M = int(input())

    matrix = []

    for i in range(0, N):
        podlist = [int(element) for element in input().split(" ")]
        matrix.append(podlist)

    matrix = [[multiply(matrix[i][j], i, N) for j in range(M)] for i in range(N)]

    print(matrix)
