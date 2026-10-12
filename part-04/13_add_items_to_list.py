items = int(input("How many items: "))
list_items = []

i = 0

while i < items:
    i += 1
    item = int(input(f"Item {i}: "))
    list_items.append(item)

print(list_items)