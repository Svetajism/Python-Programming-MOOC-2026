def squared(word, size):
    row = word * size ** 2
    i = 0
    while i < size:
        print(row[size * i: ((size * i) + size)])
        i += 1


# def squared(word, size):
#     row = word * size ** 2
#     length = 0
#     i = 1
#     while i <= size:
#         print(row[length: i * size])
#         i += 1
#         length += size