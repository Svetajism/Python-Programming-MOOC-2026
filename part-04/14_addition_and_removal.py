list_of_numbers = []

while True:
    print(f"The list is now {list_of_numbers}")
    action = input("a(d)d, (r)emove or e(x)it: ")

    if action == "d":
        list_of_numbers.append(len(list_of_numbers) + 1)
        
    elif action == "r" and len(list_of_numbers) > 0:
        list_of_numbers.pop()
       
    elif action == "x":
        print("Bye!")
        break