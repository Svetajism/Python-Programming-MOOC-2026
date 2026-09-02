name = input('Please tell me your name: ')

if name != 'Jerry':
    soup_count = int(input('How many portions of soup? '))
    cost = 5.90 * soup_count
    print(f'The total cost is {cost}')

print('Next please!')