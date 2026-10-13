def list_of_stars(my_list : list):
    for item in my_list:
        print("*" * item)

# Test function
if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])