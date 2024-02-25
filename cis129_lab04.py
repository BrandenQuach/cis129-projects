# Author: Branden Quach
# Calculates company bonuses

# Declare local variables
monthlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0
prompt = 'Monthly sales?'

# This code gets the monthly sales
monthlySales = float(input(prompt))

# This code determines the storeAmount bonus
if monthlySales >= 110000:
  storeAmount = 6000
elif monthlySales >= 100000:
  storeAmount = 5000
elif monthlySales >= 90000:
  storeAmount = 4000
elif monthlySales >= 80000:
  storeAmount = 3000
else:
  storeAmount = 0

# This code gets the percent of increase in sales
salesIncrease = float(input('Percentage of sales increase?')
salesIncrease = salesIncrease / 100

# This code determines the empAmount bonus
if salesIncrease >= .05:
  empAmount = 75
elif salesIncrease >= .04:
  empAmount = 50
elif salesIncrease >= .03:
  empAmount = 40
else:
  empAmount = 40

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) AND (empAmount == 75):
  print('Congrats! You have reached the highest bonus amounts possible!')
