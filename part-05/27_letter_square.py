letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


layers = int(input("Layers: "))
chars = letters[:layers]
side_size = layers * 2 - 1
centre = side_size // 2


for i in range(side_size):
    row = []
    ver = abs(i - centre)
    for j in range(side_size):
        hor = abs(j - centre)
        row.append(chars[max(ver, hor)])
    print("".join(row))