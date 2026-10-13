# Write your solution here
def shortest(words: list):
    shortest_word = words[0]
    for item in words:
        if len(item) < len(shortest_word):
            shortest_word = item
    
    return shortest_word



# Test function
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)