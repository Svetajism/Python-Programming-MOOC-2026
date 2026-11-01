def transpose(matrix: list):

    for i in range(len(matrix)):
        for j in range(i + 1,len(matrix)):
            # print(f"CURRENT ELEMENT: {matrix[i][j]}")
            # print(f"I: {i}")
            # print(f"J: {j}")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# flip x and y
# x = []
# y = [][]


# Test
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    print(matrix)

    m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
    transpose(m)
    print(m)