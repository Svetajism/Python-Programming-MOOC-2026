def sum_of_positives(my_list: list):
    total = 0    
    for item in my_list:
        if item >= 0:
            total += item
    return(total)


# Test function
if __name__ == "__main__":
    my_list = [1, -1, 2, -2, 3, -3]
    result = sum_of_positives(my_list)
    print("The result is", result)