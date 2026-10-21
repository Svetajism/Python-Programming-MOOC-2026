def most_common_character(phrase: str):
    most_frequent = phrase[0]
    for char in phrase:
        if phrase.count(char) > phrase.count(most_frequent):
            most_frequent = char
    
    return most_frequent

# Test function
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string)) # b

    second_string = "exemplaryelementary"
    print(most_common_character(second_string)) # e