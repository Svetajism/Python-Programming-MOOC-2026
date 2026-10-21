def longest_series_of_neighbours(numbers: list):

    count = 1
    maximum = 1

    for index in range(len(numbers) - 1):

        if numbers[index + 1] - numbers[index] == 1 or numbers[index] - numbers[index + 1] == 1:
            count += 1

        else:
            count = 1

        maximum = max (maximum, count)

    return maximum