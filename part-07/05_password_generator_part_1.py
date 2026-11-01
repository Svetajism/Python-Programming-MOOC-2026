import random
import string

def generate_password(length: int):
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_lowercase)
    return password

# Test
if __name__ == "__main__":
    print(generate_password(12))