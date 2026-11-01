# asks the user for the names of these two files, 
# reads the files, 
# and then prints out the total number of exercises completed by each student.


# def read_students():
#     with open("students1.csv") as new_file:
#         students = {}
#         for line in new_file:
#             line = line.replace("\n", "")
#             parts = line.split(";")
#             if parts[0] == 'id':
#                 continue
#             full_name = parts[1] + " " + parts[2]
#             students[parts[0]] = full_name
#     # print(data)
#     return students

# def read_exercises():
#     with open("exercises1.csv") as new_file:
#         exercises = {}
#         for line in new_file:
#             parts = line.split(";")
#             amount = []
#             if parts[0] == 'id':
#                 continue
#             for part in parts[1:]:
#                 number = int(part)
#                 amount.append(number)
#             exercises[parts[0]] = amount
#     return exercises


if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students = {}

with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        full_name = parts[1] + " " + parts[2]
        students[parts[0]] = full_name


exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        amount = []
        if parts[0] == 'id':
            continue
        for part in parts[1:]:
            number = int(part)
            amount.append(number)
        exercises[parts[0]] = amount


for id, name in students.items():
    if id in exercises:
        total = sum(exercises[id])
        print(f"{name} {total}")
    else:
        print(f"{name:16} 0 exercises")