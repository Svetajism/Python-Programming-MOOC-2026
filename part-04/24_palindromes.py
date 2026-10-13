def palindromes(word : str):
    list1 = list(word)
    list2 = list(word)
    list2.reverse()
    return list1 == list2

while True:
    word = input("Please type in a palindrome: ")
    
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    
    print("that wasn't a palindrome")

# Test function
if __name__ == "__main__":
    print(palindromes("python"))
    print(palindromes("level"))