def histogram(my_str: str):
    letters = {}
    for char in my_str:
        # print(char)
        if char not in letters:
            letters[char] = 0
        letters[char] += 1

    for key, value in letters.items():
        print(f"{key} {'*' * value}")


# print(histogram("abba"))
# print(histogram("statistically"))



if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")
