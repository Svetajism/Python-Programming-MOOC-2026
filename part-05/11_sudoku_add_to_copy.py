# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        row = sudoku[i]
        if i > 0 and i % 3 == 0:
            print()
        for j in range(len(row)):
            if j > 0 and j % 3 == 0:
                print(" ", end="")
            if row[j] == 0:
                print("_", end=" ")
            else:
                print(row[j], end=" ")
        print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []

    for row in sudoku:
        sudoku_copy.append(row[:])
    
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy



    # for i in range(len(sudoku)):
    #     row = sudoku[i]
    #     row_copy = []
    #     sudoku_copy.append(row_copy)
    #     for item in row:
    #         row_copy.append(item)
    # sudoku_copy[row_no][column_no] = number
    # return sudoku_copy



if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)