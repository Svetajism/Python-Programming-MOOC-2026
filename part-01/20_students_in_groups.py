students_total = int(input('How many students on the course? '))
group_size = int(input('Desired group size? '))

group_final = students_total // group_size

if students_total % group_size > 0:
    group_final += 1

print(f'Number of groups formed: {group_final}')


# second option
students_total_2 = int(input('How many students on the course? '))
group_size_2 = int(input('Desired group size? '))

group_final_2 = (students_total_2 + group_size_2 - 1 )// group_size_2

print(f'Number of groups formed: {group_final_2}')

