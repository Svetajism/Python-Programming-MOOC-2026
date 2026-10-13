def distinct_numbers(numbers: list):
    new_numbers = []
    for item in numbers:
        if item not in new_numbers:
            new_numbers.append(item)
    
    return sorted(new_numbers)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]