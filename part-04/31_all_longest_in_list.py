def all_the_longest(words: list):
    longest_words = []
    biggest = words[0]
    for item in words:
        if len(item) > len(biggest):
            longest_words.clear()
            biggest = item
            longest_words.append(biggest)
        elif len(item) == len(biggest):
            longest_words.append(biggest)

    return longest_words


# model solution:
# def all_the_longest(names: list):
#     result = []
 
#     for name in names:
#         if result == [] or len(name) > len(result[0]):
#             result = [name]
#         elif len(name) == len(result[0]):
#             result.append(name)
 
#     return result


# Test function
if __name__ == "__main__":
    my_list = ["aaa", "bb", "ccc", "dddd", "ee", "ffff"]

    result = all_the_longest(my_list)
    print(result) # ['dddd', 'ffff']

    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']