string_input = input("Please type in a string: ")
substring_input = input("Please type in a substring: ")

i = string_input.find(substring_input)
i = string_input.find(substring_input, i + len(substring_input))

if i != -1:
    print(f"The second occurrence of the substring is at index {i}.")
else:
    print("The substring does not occur twice in the string.")