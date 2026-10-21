def everything_reversed(words: list):
    reversed_words = []
    for word in words:
        new_word = word[::-1]
        reversed_words.append(new_word)
    return reversed_words[::-1]

# Test function
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)