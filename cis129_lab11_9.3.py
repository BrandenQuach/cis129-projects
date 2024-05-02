# Lab 11 9.3: Student Records into CSV
# Author: Branden Quach
# May 1, 2024
# Allow entry of names and grades associated into CSV file format.

# Import CSV library
import csv

# Opens grades.csv file in write mode
with open('grades.csv', mode='w') as grades:
    # while loop
    while True:
        # Prompts first and last name
        first = input(f'Enter first name: ')
        last = input(f'Enter last name: ')
        # Try loop to catch non integer values
        try:
            # Prompts integer values for exam grades
            exam1 = int(input(f'Enter grade for exam 1: '))
            exam2 = int(input(f'Enter grade for exam 2: '))
            exam3 = int(input(f'Enter grade for exam 3: '))
        except:
            print(f'An integer was not entered.')
        # Prints values into CSV file
        print(f'{first},{last},{exam1},{exam2},{exam3}', file=grades)
        # Prompt to end or continue program
        end = input(f'Enter -1 to quit or press any key to continue.')
        if end == '-1':
            break
