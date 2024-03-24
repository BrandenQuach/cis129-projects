# Lab 6: Hot Dog Cookout Calculator
# Author: Branden Quach
# March 23, 2024
# Displays hotdog amounts given by input

import math

def main():
    # Get total number of hotdogs
    total = getTotalHotdogs()

    # Constants
    dogs = 8 # Hotdogs in a package
    buns = 10 # Hotdog buns in a package

    # Variables
    dogsLeft = 0 # Left over hotdogs
    bunsLeft = 0 # Left over hotdog buns
    minDogs = 0 # Minimum packages of hotdogs
    minBuns = 0 # Minimum packages of hotdog buns

    # Calculate leftover hotdogs
    dogsLeft = (dogs - total % dogs) % dogs

    # Calculate minimum number of packages of hotdogs
    minDogs = math.ceil(total / dogs)

    # Calculate leftover hotdog buns
    bunsLeft = (buns - total % buns) % buns

    # Calculate minimum number  of packages of hotdog buns
    minBuns = math.ceil(total / buns)

    # Display the results
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

def getTotalHotdogs():
    # Variables
    people = 0
    hotdogs = 0

    # Prompts
    people = (int(input(f'Enter the number of people attending the cookout: ')))
    hotdogs = (int(input(f'Enter the number of hotdogs for each person: ')))

    # Calculations
    total = people * hotdogs
    return total
# Display the results
def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    print(f'Minimum packages of hotdogs needed: ', minDogs)
    print(f'Minimum packages of hotdog buns needed: ', minBuns)
    print(f'Hotdogs left over: ', dogsLeft)
    print(f'Hotdog buns left over: ', bunsLeft)
if __name__==  "__main__":
    main()

