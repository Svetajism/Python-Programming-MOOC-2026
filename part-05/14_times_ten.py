def times_ten(start_index: int, end_index: int):
    values = {}
    for item in range(start_index, end_index + 1):
        print(item)
        values[item] = item * 10
    return values

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)