phrase = ""
previous_word = ""

while True:
    last_word = input("Please type in a word: ")

    if last_word == "end" or previous_word == last_word:
        break

    phrase += last_word + " "
    previous_word = last_word

print(phrase)