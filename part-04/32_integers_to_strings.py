def formatted(numbers: list):
    result = []
    for number in numbers:
        number_new = f"{number:.2f}"
        result.append(number_new)
    return result


# Test function
if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list) # ['1.23', '0.33', '0.11', '3.45']