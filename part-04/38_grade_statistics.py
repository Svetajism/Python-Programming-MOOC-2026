def read_results():
    # Read input lines until the user enters an empty line.
    # Returns two lists: exam points and completed exercises, one value per student.

    exam_points = []
    exercises = []
    
    while True:
        user_input = input("Exam points and exercises completed: ")

        if user_input == "":
            break

        one_student_data = user_input.split()
        exam_points.append(int(one_student_data[0]))
        exercises.append(int(one_student_data[1]))

    return exam_points, exercises


def exercise_points(exercises):
    # One student: every full 10% of exercises gives 1 point (rounded down).
    return exercises // 10


def grade(exam, total):
    # One student: returns a grade from 0 to 5.
    # Exam cutoff: less than 10 exam points means an automatic fail.
    if exam < 10:
        return 0

    # (minimum total points, grade), checked from the highest grade down
    thresholds = [
        (28, 5),
        (24, 4),
        (21, 3),
        (18, 2),
        (15, 1),
    ]

    for min_points, grade_value in thresholds:
        if total >= min_points:
            return grade_value

    # Total is below 15: fail
    return 0


def points_average(totals):
    # Average of all students' total points.
    return sum(totals) / len(totals)

def pass_percentage(grades):
    # Percentage of students who passed the course (grade above 0).
    count = 0
    for g in grades:
        if g > 0:
            count += 1
    return (count / len(grades)) * 100


def grade_distribution(grades):
    # Counts how many students got each grade.
    # The list index is the grade: distribution[3] = number of students with grade 3.
    distribution = [0, 0, 0, 0, 0, 0]
    for g in grades:
        distribution[g] += 1
    return distribution
        
    

def print_statistics(average, percentage, distribution):
    # The only place where statistics are printed.
    # Floats are shown with one decimal place.
    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {percentage:.1f}")
    print("Grade distribution:")

    # Print grades from 5 down to 0, one star per student
    for i in range(5, -1, -1):
        print(f"  {i}: {'*' * distribution[i]}")


def main():
    # 1. Collect input
    exam_points, exercises = read_results()

    # 2. Calculate total points and grade for each student
    # (the same index in both lists belongs to the same student)
    totals = []
    grades = []
    for i in range(len(exercises)):
        totals.append(exam_points[i] + exercise_points(exercises[i]))
        grades.append(grade(exam_points[i], totals[i]))
        

    # 3. Calculate statistics and print them
    average = points_average(totals)
    percentage = pass_percentage(grades)
    distribution = grade_distribution(grades)
    print_statistics(average, percentage, distribution)


main()