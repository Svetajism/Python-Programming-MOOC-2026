def list_sum(numbers1: list, numbers2: list):
    totals = []
    for i in range(len(numbers1)):
        totals.append(numbers1[i] + numbers2[i])

    return totals


# Test function
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]