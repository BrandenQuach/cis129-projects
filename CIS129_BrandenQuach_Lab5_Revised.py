# Lab 5: The Bottle Return Program
# Author: Branden Quach
# March 19, 2024
# Collects bottle amounts per week to show the total payout.

# Declare Variables
totalBottles = 0
counter = 1
totalPayout = 0
todayBottles = 0
keepGoing = 'y'

# Loop to run program again
while keepGoing == 'y':
  # Code to set values of variables
  totalBottles = 0
  totalPayout = 0
  counter = 1
  for counter in range(7):
    todayBottles = (int(input(f'Enter number of bottles for day #{counter}: ')))
    totalBottles = totalBottles + 1
    counter = counter + 1
    totalPayout = totalBottles * 0.1

# Prints final results
print()
print(f'The total number of bottles collected is {totalBottles}')
print(f'The total paid out is ${totalPayout: .2f}')
print()

# Prompts for another week of data
print("Do you want to enter another week's worth of data?")
keepGoing = (input('(Enter y or n): '))
