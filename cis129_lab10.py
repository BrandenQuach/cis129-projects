# Lab 10: Check Protection
# Author: Branden Quach
# April 27, 2024
# Prints input into a check protected format

# Variable for the amount of characters in check format
field = 11

# Main function
def main():
    # Calls function to receive input
    getAmount = getValidAmount()
    # Formats input into the 2 decimal dollar amount
    formattedAmount = '{:.2f}'.format(getAmount)
    # Adds asterisk to fill empty characters
    checkAmount = f'{formattedAmount:*>{field}}'
    # Outputs check protected format
    print(f'Your input in check protected format is: \n$ {checkAmount}')

# Function that receives input
def getValidAmount():
    # Try except block to catch errors
    try:
        # Prompt
        getAmount = (float(input(f'Enter the dollar amount:')))
        # Checks for negative numbers
        if getAmount < 0:
            print(f'{getAmount} is not a valid entry. Please try again.')
            return getValidAmount()
        else:
            return getAmount
    # Prompts again due to input error
    except:
        print(f'Invalid entry. Please try again.')
        return getValidAmount()
# Calls main function
main()
