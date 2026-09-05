year = int(input("Please type in a year: "))
candidate = year + 1

while True:
    if (candidate % 4 == 0 and candidate % 100 != 0) or candidate % 400 == 0:
        break

    candidate += 1

print(f"The next leap year after {year} is {candidate}")