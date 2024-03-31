# Lab 7: Theater Seating
# Author: Branden Quach
# March 30. 2024
# Displays number of tickets and income sold in a theater

# Libraries
import string

# Main function
def main():
    # Variables
    endProgram = 'YES'
    sectionA = 20 # Cost of one ticket in section A
    sectionB = 15 # Cost of one ticket in section B
    sectionC = 10 # Cost of one ticket in section C
    sectionAseats = 300
    sectionBseats = 500
    sectionCseats = 200
    totalticketsSold = 0
    totalIncome = 0
    while endProgram == 'Y' or endProgram == 'YE' or endProgram == 'YES':
        print()
        # Local Variables
        seatsA = 0 # Tickets sold in section A
        seatsB = 0 # Tickets sold in section B
        seatsC = 0 # Tickets sold in section C
        ticketsSold = 0
        income = 0
        # Section seat amounts and costs
        print(f'Section A seats:', sectionAseats, 'at $', sectionA)
        print(f'Section B seats:', sectionBseats, 'at $', sectionB)
        print(f'Section C seats:', sectionCseats, 'at $', sectionC)
        # Call to calculate seats sold
        seatsA = seatsSoldA(seatsA, sectionAseats)
        seatsB = seatsSoldB(seatsB, sectionBseats)
        seatsC = seatsSoldC(seatsC, sectionCseats)
        # Call to calculate tickets sold and income
        ticketsSold = inputTickets(seatsA, seatsB, seatsC)
        income = price(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC)
        # Logs session totals
        totalticketsSold += ticketsSold
        totalIncome += income
        # Calculates seats left
        sectionAseats -= seatsA
        sectionBseats -= seatsB
        sectionCseats -= seatsC
        # Calls receipt  and seats left function
        receipt(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC, ticketsSold, income, totalticketsSold, totalIncome)
        seatsLeft(sectionAseats, sectionBseats, sectionCseats)
        # Calls to prompt a program ending
        endProgram = upperendProgram()
# Prompts seats sold and detects valid input
def seatsSoldA(seatsA, sectionAseats):
    seatsA = (int(input(f'Enter the number of seats sold in section A: ')))
    while seatsA > sectionAseats:
        print(f'Invalid number entered')
        seatsA = (int(input(f'Enter the number of seats sold in section A: ')))
    return seatsA
def seatsSoldB(seatsB, sectionBseats):
    seatsB = (int(input(f'Enter the number of seats sold in section B: ')))
    while seatsB > sectionBseats:
        print(f'Invalid number entered')
        seatsB = (int(input(f'Enter the number of seats sold in section B: ')))
    return seatsB
def seatsSoldC(seatsC, sectionCseats):
    seatsC = (int(input(f'Enter the number of seats sold in section C: ')))
    while seatsC > sectionCseats:
        print(f'Invalid number entered')
        seatsC = (int(input(f'Enter the number of seats sold in section C: ')))
    return seatsC
# Calculates total tickets sold
def inputTickets(seatsA, seatsB, seatsC):
    ticketsSold = seatsA + seatsB + seatsC
    return ticketsSold
# Calculates income
def price(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC):
    income = (seatsA * sectionA) + (seatsB * sectionB) + (seatsC * sectionC)
    return income
# Prints receipt
def receipt(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC, ticketsSold, income, totalticketsSold, totalIncome):
    print()
    print(seatsA, 'seats sold in section A at $', sectionA, 'per ticket')
    print(seatsB, 'seats sold in section B at $', sectionB, 'per ticket')
    print(seatsC, 'seats sold in section C at $', sectionC, 'per ticket')
    print()
    print(f'The amount of tickets sold is: ', ticketsSold)
    print(f'The income is: $', income)
    print(f'The total amount of tickets sold is: ', totalticketsSold)
    print(f'The total income is: $', totalIncome)
# Prints session totals
def seatsLeft(sectionAseats, sectionBseats, sectionCseats):
    print()
    print(f'The seats remaining is:')
    print(f'Section A:', sectionAseats)
    print(f'Section B:', sectionBseats)
    print(f'Section C:', sectionCseats)
# Determines if entry for yes/no loop is valid
def upperendProgram():
    touppercase = input(f'Do you want to enter more data? (YES/NO): ')
    endProgram = touppercase.upper()
    if endProgram == 'Y' or endProgram == 'YE' or endProgram == 'YES' or endProgram == 'N' or endProgram == 'NO':
        return endProgram
    else:
        print(f'Invalid entry')
    
main()
