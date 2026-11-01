# Write your solution here
def remove_smallest(numbers: list):
    smallest = numbers[0]
    for i in range(len(numbers)):
        smallest = min(smallest, numbers[i])
        # if numbers[i] < smallest:
        #     smallest = numbers[i]
    numbers.remove(smallest)

    # smallest = min(numbers)
    # numbers.remove(smallest)
        
    # numbers.sort()
    # numbers.pop(0)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)