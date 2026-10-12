my_list = [1, 2, 3, 4, 5]
while True:
    i = int(input("Index: "))
    if i == -1:
        break
    if i < 0 or i >= len(my_list):
        print("Index is outside of the range of the list")
        continue
    value_new = int(input("New value: "))
    my_list[i] = value_new
    print(my_list)