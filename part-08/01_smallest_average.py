def average(person: dict):
    total = person["result1"] + person["result2"] + person["result3"]
    return total / 3


def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest = person1

    if average(person2) < average(smallest):
        smallest = person2

    if average(person3) < average(smallest):
        smallest = person3

    # OPTION 2
    # people = [person1, person2, person3]
    # smallest = people[0]
    # total_smallest = people[0]["result1"] + people[0]["result2"] + people[0]["result3"]
    # for person in people:
    #     total = person["result1"] + person["result2"] + person["result3"]
    #     # print(total)
    #     if total < total_smallest:
    #         total_smallest = total
    #         smallest = person
    #     # print(f"SMALLEST: {smallest}")
    return smallest



    # smallest = person1
    # take values of keys from 1 to last
    # sum the values and divide by len - 1
    # compare the average of the first to average of the second
    # compare the average of the second to thirs, etc.
    
    # pass

# Test
if __name__ == "__main__":
    # person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    # person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    # person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    person1 = {"name": "A", "result1": 3, "result2": 3, "result3": 3}  # сумма 9
    person2 = {"name": "B", "result1": 1, "result2": 1, "result3": 1}  # сумма 3
    person3 = {"name": "C", "result1": 2, "result2": 2, "result3": 2} 

    print(smallest_average(person1, person2, person3))