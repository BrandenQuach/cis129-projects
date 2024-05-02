# Lab 11 9.1: Grades to .txt
# Author: Branden Quach
# May 1, 2024
# Collects grades with totals and average into a text file.

# Opens text file in writing mode
with open('grades.txt', mode='w') as grades:
    # Variables
    total = 0
    count = 0
    # While loop for multiple entries
    while True:
        # Prompt for grade input
        grade = input(f'Enter a grade or -1 to quit: ')
        # Detects sentinel value to quit program
        if grade == '-1':
            break
        # Calculates total, count, average
        total += int(grade)
        count += 1
        average = total/count
        # prints data into text file
        print(f'{grade} {total} {count} {average}', file=grades)
