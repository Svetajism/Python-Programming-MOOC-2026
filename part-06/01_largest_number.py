def largest():
    with open("numbers.txt") as numbers:
        start = True
        largest_number = 0

        for number in numbers:
            if start or int(number) > largest_number:
                largest_number = int(number)
                start = False

            # number = int(number)
            # largest_number = max(largest_number, number)
    return largest_number


# def smallest():
#     with open("numbers.txt") as numbers:
#         start = True
#         smallest_number = 0

#         for number in numbers:
#             print()
#             print(number)
#             print(start)
#             print(f"SMALLEST: {smallest_number}")
#             if start or int(number) < smallest_number:
#                 smallest_number = int(number)
#                 start = False

#             # number = int(number)
#             # largest_number = max(largest_number, number)
#     # print(smallest_number)
#     return smallest_number

if __name__ == "__main__":
    largest()
    # smallest()
