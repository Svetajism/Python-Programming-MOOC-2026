limit = int(input("Upper limit: "))
number = 1
total = 1
calculation = f"{number}"

while total < limit:
    number += 1
    total += number
    calculation += f" + {number}"

print(f"The consecutive sum: {calculation} = {total}")
