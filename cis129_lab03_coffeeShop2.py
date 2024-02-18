# Author: Branden Quach
# Receipt for a coffee shop simulator

# Constants
priceofcoffee = 5
priceofmuffin = 4
tax = 0.06

# Displays Prompts
print ('***************************************')
print ('My Coffee and Muffin Shop')
coffeeamount = int(input('Number of coffees bought?'))
muffinamount = int(input('Number of muffins bought?'))
print ('***************************************')
print ('***************************************')

# Equations
coffeecost = coffeeamount * 5
muffincost = muffinamount * 4
taxamount = tax * (coffeecost + muffincost)

# Displays Amounts
print ('My Coffee and Muffin Shop Receipt')
print (coffeeamount ,'Coffee at $5 each: $', coffeecost)
print (muffinamount ,'Muffin at $4 each: $', muffin cost)
print ('6% tax: $', taxamount)

# Calculates Total
totalcost = coffeecost + muffincost + taxamount

# Displays Total
print ('---------')
print ('Total: $', totalcost)
print ('***************************************')
