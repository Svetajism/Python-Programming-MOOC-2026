# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.count_numbers() == 0:
            return 0
        avg = self.get_sum() / self.count_numbers()
        return avg


def statistics():
    stats = NumberStats()
    even = NumberStats()
    odd = NumberStats()
    while True:
        number = int(input("Please type in integer numbers: "))
        if number == -1:
            print(f"Sum of numbers: {stats.get_sum()}")
            print(f"Mean of numbers: {stats.average()}")
            print(f"Sum of even numbers: {even.get_sum()}")
            print(f"Sum of odd numbers: {odd.get_sum()}")
            break
        stats.add_number(number)
        if number % 2 == 0:
            even.add_number(number)
        else:
            odd.add_number(number)


statistics()