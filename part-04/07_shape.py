def line(length, character):
    if character == "":
        character = "*"
    print(length * character[0])

def shape(width, triangle_char, rect_height, rect_char):
    i = 0
    while i < width:
        i += 1
        line(i, triangle_char)
    
    j = 0
    while j < rect_height:
        j += 1
        line(width, rect_char)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")