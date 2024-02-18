# Author: Branden Quach
# Receipt for a coffee shop simulator

# Constants
priceofcoffee = 5
priceofmuffin = 4
priceoftea = 3
priceofbagel = 5
tax = 0.06

# Displays Prompts
print ('***************************************')
print ("Branden's Cafe")
coffeeamount = int(input('Number of coffees bought?'))
muffinamount = int(input('Number of muffins bought?'))
teaamount = int(input('Number of teas bought?'))
bagelamount = int(input('Number of bagels bought?'))
print ('***************************************')
print ('***************************************')

# Equations
coffeecost = coffeeamount * 5
muffincost = muffinamount * 4
teacost = teaamount * 3
bagelcost = bagelamount * 5
taxamount = tax * (coffeecost + muffincost + teacost + bagelcost)

# Displays Amounts
print ("Branden's Cafe Receipt")
print (coffeeamount ,'Coffee at $5 each: $', coffeecost)
print (muffinamount ,'Muffin at $4 each: $', muffincost)
print (teaamount ,'Tea at $3 each: $', teacost)
print (bagelamount ,'Bagel at $5 each: $', bagelcost)
print ('6% tax: $', taxamount)

# Calculates Total
totalcost = coffeecost + muffincost + teacost + bagelcost + taxamount

# Displays Total
print ('---------')
print ('Total: $', totalcost)
print ('Thank you for your purchase! :)')
print ('***************************************')
