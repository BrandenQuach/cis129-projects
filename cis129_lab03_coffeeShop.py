# Author: Branden Quach
# Receipt for a coffee shop simulator

Declare Integer numberOfCoffeePurchased
Declare Integer numberOfMuffinPurchased
Declare Real priceOfCoffee
Declare Real priceOfMuffin

print('***************************')
print('My Coffee and Muffin Shop')
Display "Number of coffees bought?"
Input numberOfCoffeePurchased
Display "Number of muffins bought?"
Input numberOfMuffinPurchased
print('***************************')

Declare Real totalCoffeeCost
totalCoffeeCost = numberOfCoffeePurchased * 5
Declare Real totalMuffinCost
totalMuffinCost = numberOfMuffinPurchased * 4
Declare Real totalTaxCost
totalTaxCost = (totalCoffeeCost + totalMuffinCost) * 0.06
Declare Real totalCost
totalCost = totalCoffeeCost + totalMuffinCost + totalTaxCost

print('***************************')
print('My Coffee and Muffin Shop Receipt')
Display numberOfCoffeePurchased , "Coffee at $5 each: $ " , totalCoffeeCost
Display numberOfMuffinPurchased , "Muffin at $4 each: $ " , totalMuffinCost
Display "6% tax: " , totalTaxCost
print('---------')
Display "Total: $ " , totalCost
print('***************************')
