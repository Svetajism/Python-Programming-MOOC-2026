word = input("Please type in a string: ")

empty = 30 - len(word) - 2
left = " " * (empty // 2)
right = " " * (empty // 2)

if empty % 2 != 0:
    right += " " 

center = "*" + left + word + right + "*"

print("*" * 30)
print(center)
print("*" * 30)