a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")

if (a > b and a < c) or (a > c and a < b):
    middle_letter = a
elif (b > a and b < c) or (b > c and b < a):
    middle_letter = b
else:
    middle_letter = c 

print("The letter in the middle is", middle_letter)