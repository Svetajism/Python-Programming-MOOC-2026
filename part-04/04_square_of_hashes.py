def line(length, character):
    if character == "":
        character = "*"
    print(length * character[0])

def square_of_hashes(size):
    i = 0
    while i < size:
        line(size, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(6)