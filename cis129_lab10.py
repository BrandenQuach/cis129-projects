# Lab 10: Check Protection
# Author: Branden Quach
# April 27, 2024
# Prints number into a check protected format

field = 11

def main():
    getAmount = getValidAmount()
    formattedAmount = '{:.2f}'.format(getAmount)
    checkAmount = f'{formattedAmount:*>{field}}'
    print(f'Your input in check protected format is: \n$ {checkAmount}')
def getValidAmount():
    try:
        getAmount = (float(input(f'Enter the dollar amount:')))
        if getAmount < 0:
            print(f'{getAmount} is not a valid entry. Please try again.')
            return getValidAmount()
        else:
            return getAmount
    except:
        print(f'Invalid entry. Please try again.')
        return getValidAmount()
main()
