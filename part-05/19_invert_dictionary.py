def invert(dictionary: dict):
    original = dictionary.copy()
    dictionary.clear()
    for key, value in original.items():
        dictionary[value] = key


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)