# Lab 7: Theater Seating
# Author: Branden Quach
# March 29. 2024
# Displays number of tickets and income sold in a theater

# Main function
def main():
    # Variables
    endProgram = 'no'
    sectionA = 20 # Cost of one ticket in section A
    sectionB = 15 # Cost of one ticket in section B
    sectionC = 10 # Cost of one ticket in section C
    sectionAseats = 300
    sectionBseats = 500
    sectionCseats = 200
    totalticketsSold = 0
    totalIncome = 0
print(f'Section A: 
    while endProgram == 'no':
        # Local Variables
        seatsA = 0 # Tickets sold in section A
        seatsB = 0 # Tickets sold in section B
        seatsC = 0 # Tickets sold in section C
        ticketsSold = 0
        income = 0
        # Call to calculate seats sold
        seatsA = seatsSoldA(seatsA)
        seatsB = seatsSoldB(seatsB)
        seatsC = seatsSoldC(seatsC)
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

        receipt(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC, ticketsSold, income, totalticketsSold, totalIncome)
        seatsLeft(sectionAseats, sectionBseats, sectionCseats)
        
        endProgram = input(f'Do you want to end the program? (yes/no): ')
# Prompts seats sold
def seatsSoldA(seatsA):
    seatsA = (int(input(f'Enter the number of seats sold in section A: ')))
    return seatsA
def seatsSoldB(seatsB):
    seatsB = (int(input(f'Enter the number of seats sold in section B: ')))
    return seatsB
def seatsSoldC(seatsC):
    seatsC = (int(input(f'Enter the number of seats sold in section C: ')))
    return seatsC
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
    print()
    print(f'The total amount of tickets sold is: ', totalticketsSold)
    print(f'The total income is: $', totalIncome)
# Prints session totals
def seatsLeft(sectionAseats, sectionBseats, sectionCseats):
    print()
    print(f'The seats remaining is:')
    print(f'Section A:', sectionAseats)
    print(f'Section B:', sectionBseats)
    print(f'Section C:', sectionCseats)
    
main()
