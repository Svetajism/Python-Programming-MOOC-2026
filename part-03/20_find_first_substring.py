word = input("Please type in a word: ")
character = input("Please type in a character: ")

i = word.find(character)

if len(word) - i >= 3:
    print(word[i:i+3])
