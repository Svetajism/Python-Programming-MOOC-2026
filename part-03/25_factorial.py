while True:
    number = int(input("Please type in a number: "))
    
    if number <= 0:
        print("Thanks and bye!")
        break
    
    count = 1
    factorial = 1
    
    while count <= number:
        print(f"COUNT: {count}")
        factorial *= count 
        count += 1
        print(f"RESULT: {factorial}")


    print(f"The factorial of the number {number} is {factorial}")