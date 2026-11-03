# OPTION 1
def sum_of_elements(numbers: list):
    total = 0
    for number in numbers:
        total += number
        print(numbers)
    return total

def row_sums(my_matrix: list):
    for numbers in my_matrix:
        element = sum_of_elements(numbers)
        print(element)
        numbers.append(element)
        print(f"NUMBERS: {numbers}")



# OPTION 2
def row_sums2(my_matrix: list):
    for row in my_matrix:
        row.append(sum(row))


# Test
if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)