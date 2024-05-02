# Lab 11 9.2: Reading Grades
# Author: Branden Quach
# May 1, 2024
# Reads grade.txt file.

# Opens grades.txt file in read mode
with open('grades.txt', mode='r') as grades:
    # Prints header for identification
    print(f'{"Grade":<10}{"Total":<10}{"Count":<10}{"Average":<10}')

    for record in grades:
        # Splits text line
        grade, total, count, average = record.split()
        # Prints text
        print(f'{grade:<10}{total:<10}{count:<10}{average:<10}')
