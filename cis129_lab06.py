# Lab 6: Hot Dog Cookout Calculator
# Author: Branden Quach
# March 23, 2024
# Displays hotdog amounts given by input

import math

def main():
    # Get total number of hotdogs
    total = totalHotdogs

    # Constants
    dogs = 8 # Hotdogs in a package
    buns = 10 # Hotdog buns in a package

    # Variables
    int dogsLeft = 0 # Left over hotdogs
    int bunsLeft = 0 # Left over hotdog buns
    int minDogs = 0 # Minimum packages of hotdogs
    int minBuns = 0 # Minimum packages of hotdog buns

    # Calculate leftover hotdogs
    dogsLeft = (dogs - total % dogs) % dogs

    # Calculate minimum number of packages of hotdogs
    minDogs = math.ceil(total / dogs)

    # Calculate leftover hotdog buns
    bunsLeft = (buns - total % buns) % buns

    # Calculate minimum number  of packages of hotdog buns
    minBuns = math.ceil(total / buns)

    # Display the results
    print(f'Leftover hotdogs: {dogsLeft}')
    print(f'Minimum amount of hotdog packages: {minDogs}')
    print(f'Leftover hotdog buns: {bunsLeft}')
    print(f'Minimum amount of hotdog bun packages: {minBuns}')

def getTotalHotdogs():
    
