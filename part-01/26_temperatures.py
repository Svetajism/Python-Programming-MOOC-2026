F = int(input('Please type in a temperature (F): '))
C = (F - 32) / 1.8

print(f'{F} degrees Fahrenheit equals {C} degrees Celsius')

if C < 0:
    print('Brr! It\'s cold in here!')