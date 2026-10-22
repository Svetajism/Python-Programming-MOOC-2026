# option 1
def column_correct(sudoku: list, column_no: int):
    numbers = []

    for row in sudoku:
        number = row[column_no]
        numbers.append(number)

        # print()
        # print(number)
        # print(numbers)

        
    for number in numbers:
        if number > 0 and numbers.count(number) > 1:
            return False

    return True


# option 2
def column_correct2(sudoku: list, column_no: int):
    numbers = []

    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        
        numbers.append(number)

        # print()
        # print(number)
        # print(numbers)

    return True


# Test
if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]


    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))
    print(column_correct(sudoku, 2))
    print(column_correct(sudoku, 3))
    print(column_correct(sudoku, 4))
    print(column_correct(sudoku, 5))
    print(column_correct(sudoku, 6))
    print(column_correct(sudoku, 7))
    print(column_correct(sudoku, 8))

    print(column_correct2(sudoku, 0))
    print(column_correct2(sudoku, 1))
    print(column_correct2(sudoku, 2))
    print(column_correct2(sudoku, 3))
    print(column_correct2(sudoku, 4))
    print(column_correct2(sudoku, 5))
    print(column_correct2(sudoku, 6))
    print(column_correct2(sudoku, 7))
    print(column_correct2(sudoku, 8))
