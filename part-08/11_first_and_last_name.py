# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.name = name

    def return_first_name(self):
        name = self.name
        first_name = ""
        for char in name:
            if char == " ":
                break
            first_name += char
        return first_name

    def return_last_name(self):
        name = self.name
        words = name.partition(" ")
        last_name = words[2]
        return last_name
    

# Test
if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())