def add_student(students: dict, name: str):
    students[name] = []
    return students

def average(courses: list):
    if len(courses) == 0:
        return
    total = 0
    for course in courses:
        total += course[1]
    avg = total / len(courses)

    return avg


def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
    print(f"{name}:")
    courses = students[name]
    if len(courses) == 0:
        print(" no completed courses")
        return
    print(f" {len(courses)} completed courses:")
    avg = average(students[name])
    for course in courses:
        print(f"  {course[0]} {course[1]}")
    print(f" average grade {avg}")


def add_course(students: dict, name: str, course: tuple):
    if course[1] <= 0:
        return
    if name in students:
        course_title = course[0]
        for i in range(len(students[name])):
            old = students[name][i]
            if old[0] == course_title:
                if old[1] < course[1]:
                    students[name][i] = course
                return

        students[name].append(course)
    

def summary(students: dict):
    print(f"students {len(students)}")

    most_courses = 0
    most_courses_name = ""

    best_avg = 0
    best_avg_name = ""

    for name in students:  # noqa: PLC0206
        courses = students[name]

        if len(courses) > most_courses:
            most_courses = len(courses)
            most_courses_name = name

        avg = average(courses)
        if avg > best_avg:
            best_avg = avg
            best_avg_name = name

    print(f"most courses completed {most_courses} {most_courses_name}")
    print(f"best average grade {best_avg} {best_avg_name}")






# test
if __name__ == "__main__":
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")




    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
