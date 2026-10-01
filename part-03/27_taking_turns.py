number = int(input("Please type in a number: "))

index = 1
while index < number:
    print(index)
    print(number)
    index += 1
    number -= 1

if index == number:
    print(number)