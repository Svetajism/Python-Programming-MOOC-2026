phone_book = {}
while True:
    command = input("command (1 search, 2 add, 3 quit): ")
   
    if command == "1":
        name_search = input("name: ")
        if name_search not in phone_book:
            print("no number")
        else:
            print(phone_book[name_search])

    elif command == "2":
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")
    
    else:
        print("quitting...")
        break