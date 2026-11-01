
# Option 1
def double_items(numbers: list):
    numbers_doubled = []
    for number in numbers:
        numbers_doubled.append(number * 2)
    return numbers_doubled

# Option 2
def double_items2(numbers: list):
    numbers_doubled2 = numbers[:]
    for i in range(len(numbers_doubled2)):
        print(i)
        numbers_doubled2[i] *= 2
    return numbers_doubled2

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)

    numbers_doubled2 = double_items2(numbers)
    print("doubled2:", numbers_doubled2)