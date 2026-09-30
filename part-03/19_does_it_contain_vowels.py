text = input("Please type in a string: ")

vovels = "aeo"
i = 0
while i < len(vovels):
    if vovels[i] in text:
        print(f"{vovels[i]} found")
    else:
        print(f"{vovels[i]} not found")
    i += 1