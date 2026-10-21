def no_vowels(phrase: str):
    vowels = "aeiou"
    result = ""
    for character in phrase:
        if character not in vowels:
            result += character
    return result



# Test function
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))