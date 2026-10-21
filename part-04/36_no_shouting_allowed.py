def no_shouting(words: list):
    low_words = []
    for word in words:
        if not word.isupper():
            low_words.append(word)
    return low_words
            

# Test function
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)