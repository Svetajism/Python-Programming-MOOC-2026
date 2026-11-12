def create_tuple(x: int, y: int, z: int):
    numbers = sorted([x, y, z])
    result = (numbers[0], numbers[-1], sum(numbers))
    return result

# test
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))