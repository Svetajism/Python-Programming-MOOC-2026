def even_numbers(numbers: list):
    even_numbers = []
    for item in numbers:
        if item % 2 == 0:
            even_numbers.append(item)
    return(even_numbers)
    
    
# Test function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)