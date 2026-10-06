def same_chars(word, i, j):
    if i >= len(word) or j >= len(word):
        return False
    return word[i] == word[j]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 6, 7))