def length_of_longest(words: list):
    best = len(words[0])

    for item in words:
        if len(item) > best:  # noqa: PLR1730
            best = len(item)
    
    return best




# Test function
if __name__ == "__main__":
    my_list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']

    result = length_of_longest(my_list)
    print(result)


    # my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    # result = length_of_longest(my_list)
    # print(result)