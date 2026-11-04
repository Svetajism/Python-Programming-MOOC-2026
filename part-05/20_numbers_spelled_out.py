def dict_of_numbers():
    all_numbers = {}
    digits = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty", 
        90: "ninety" 
    }

    for i in range(100):
        if i <= 19:
            all_numbers[i] = digits[i]

        elif i % 10 == 0:
            all_numbers[i] = tens[i]
        
        else:
            all_numbers[i] = f"{tens[i // 10 * 10]}-{digits[i % 10]}"

    return all_numbers





# Test
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])