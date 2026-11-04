phone_book = {}
while True:
    command = input("command (1 search, 2 add, 3 quit): ")
   
    if command == "1":
        name_search = input("name: ")
        if name_search not in phone_book:
            print("no number")
        else:
            for i in range(len(phone_book[name_search])):
                print(phone_book[name_search][i])

    elif command == "2":
        name = input("name: ")
        number = input("number: ")

        if name not in phone_book:
            phone_book[name] = []

        phone_book[name].append(number)

        print("ok!")
    
    else:
        print("quitting...")
        break