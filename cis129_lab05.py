# Lab 5: The Bottle Return Program
# Author: Branden Quach
# March 12, 2024
# Collects bottle amounts per week to show the total payout.

# Declare Variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = "y"

# Loop to run program again
while keepGoing == "y":
  # Code to set values of variables
  if counter % 8:
    todayBottles = int(input(f'Enter the number of bottles for day #{counter}:'))
    totalBottles = totalBottles + todayBottles
    totalPayout = totalBottles * 0.1
    counter = counter + 1
  # Code to print final results
  elif keepGoing == "y":
    print()
    print('The total number of bottles collected is', totalBottles)
    print('The total paid out is $', "%.2f" % totalPayout)
    # Code to ask for another week of input
    print()
    print("Do you want to enter another week's worth of data?")
    keepGoing = str(input('(Enter y or n): '))
    counter = 1
    totalBottles = 0
  else:
    break
