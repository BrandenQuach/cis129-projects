# Lab 5: The Bottle Return Program
# Author: Branden Quach
# March 12, 2024
# Bottle Return

# Declare Variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = "y"

# Loop to run program again
while keepGoing = "y":
  # Code to set values of variables
  totalBottles = totalBottles + todayBottles
  todayBottles = (int(input('Enter the number of bottles for day #', counter,':')))
  totalPayout = totalBottles * .1
  print('The total number of bottles collected is', totalBottles)
  print('The total paid out is $', totalPayout, end='\n')

  print("Do you want to enter another week's worth of data?")
  keepGoing = (str(input('(Enter y or n): ')))
break
