def mean(my_list: list):
    mean = sum(my_list) / len(my_list)
    return(mean)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # my_list = [3, 6, -4]
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print(result)