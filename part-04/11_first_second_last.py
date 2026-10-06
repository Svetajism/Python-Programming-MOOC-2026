def first_word(phrase):
    space = phrase.find(" ")
    return(phrase[0:space])

def second_word(phrase):
    space = phrase.find(" ")
    space2 = phrase.find(" ", space + 1)
    if space2 != -1:
        return(phrase[space + 1:space2])
    return(phrase[space+1:])  
    
def last_word(phrase):
    space = phrase.rfind(" ")
    return(phrase[space + 1:])  
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "it was"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))