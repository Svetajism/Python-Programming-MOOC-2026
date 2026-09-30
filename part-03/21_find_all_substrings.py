word = input("Please type in a word: ")
character = input("Please type in a character: ")

while True:
    i = word.find(character)
    if i == -1 or len(word) - i < 3:
        break
    print(word[i:i+3])
    word = word[i+1:]


# index option
i = 0
while i + 3 <= len(word):
    if word[i] == character:
        print(word[i:i+3])
    i += 1