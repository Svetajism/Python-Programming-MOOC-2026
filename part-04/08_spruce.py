def spruce(size):
    row = "*"
    print("a spruce!")
    i = size
    while i > 0:
        print(" " * (i - 1) + row)
        i -= 1
        row += "**"
    print(" " * (size - 1) + "*")