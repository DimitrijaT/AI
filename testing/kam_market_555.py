if __name__ == '__main__':
    R = int(input("rows:"))
    C = int(input("cols:"))

    matrix = []
    s = ''

    for i in range(R):
        a = []
        for j in range(C):
            el = int(input())
            if el != 555:
                s += f"matrix[{i}][{j}] = {el}\n"
            a.append(el)
        matrix.append(a)

    print(matrix)
    print(s)
