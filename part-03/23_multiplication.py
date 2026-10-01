# 01.10.2026

number = int(input("Please type in a number: "))
operand1 = 1

while operand1 <= number:
    operand2 = 1
    # print(operand1, operand2)
    
    while operand2 <= number:
        product = operand1 * operand2
        print(f"{operand1} x {operand2} = {product}")
        operand2 += 1

    operand1 += 1