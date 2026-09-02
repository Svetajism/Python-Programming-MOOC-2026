number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
operation = input('Operation: ')

add = number1 + number2
multiply = number1 * number2
subtract = number1 - number2

if operation == 'add':
    print(f'{number1} + {number2} = {add}')

if operation == 'multiply':
    print(f'{number1} * {number2} = {multiply}')

if operation == 'subtract':
    print(f'{number1} - {number2} = {subtract}')