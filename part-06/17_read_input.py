def read_input(prompt: str, low: int, high: int):
    while True:
        try:
            number = int(input(prompt))
            if low <= number <= high:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {low} and {high}")