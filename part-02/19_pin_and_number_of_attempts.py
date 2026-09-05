correct = 4321
attempt = 0

while True:
    pin = int(input("PIN: "))

    if pin == correct:
        break

    print("Wrong")
    attempt += 1

if attempt == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempt} attempts")
