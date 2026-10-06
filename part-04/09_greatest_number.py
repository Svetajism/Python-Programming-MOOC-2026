def greatest_number(number_1, number_2, number_3):
    biggest = number_1
    if number_2 > biggest:  # noqa: PLR1730
        biggest = number_2
    if number_3 > biggest:  # noqa: PLR1730
        biggest = number_3
    
    return(biggest)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)