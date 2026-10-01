number = int(input("Please type in a number: "))
count = 1

while count <= number:
    first = count + 1
    if first <= number:
        print(first)
    print(count)
    count += 2

# number = int(input("Please type in a number: "))
# first = 2

# while first <= number:
#     count = first - 1
#     print(first)
#     print(count)
#     first += 2