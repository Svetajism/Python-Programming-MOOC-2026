def chessboard(length):
    row = "10" * length
    count = 1
    while count <= length:
        if count %2 == 0:
            print(row[1:length + 1])
        else:
            print(row[:length])
        count += 1