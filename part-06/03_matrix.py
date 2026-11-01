def read_matrix(filename: str):
    matrix = []
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(",")
            row = []
            for part in parts:
                number = int(part)
                row.append(number)
            matrix.append(row)
    return matrix


def row_sums():
    matrix = read_matrix("matrix.txt")
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums


def matrix_sum():
    sums = row_sums()
    return(sum(sums))

    # matrix = read_matrix("matrix.txt")
    # total = 0
    # for row in matrix:
    #     total += sum(row)
    # print(total)
    # return total


def matrix_max():
    matrix = read_matrix("matrix.txt")
    row_maxes = []
    for row in matrix:
        row_maxes.append(max(row))
    return(max(row_maxes))

    


if __name__ == "__main__":
    matrix_max()
    matrix_sum()
    row_sums()
