# Lab 7: Theater Seating
# Author: Branden Quach
# March 29. 2024
# Displays number of tickets and income sold in a theater

# Libraries
import

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
    totalincome = 0

    while endProgram == 'no':
        # Local Variables
        seatsA = 0 # Tickets sold in section A
        seatsB = 0 # Tickets sold in section B
        seatsC = 0 # Tickets sold in section C
        ticketsSold = 0
        income = 0

        ticketsSold = inputTickets(seatsA, seatsB, seatsC, ticketsSold)

        income = price(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC)

        receipt(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC, ticketsSold, income)

        endProgram = input(f'Do you want to end the program? (yes/no): ')

def inputTickets(seatsA, seatsB, seatsC, ticketsSold):
    seatsA = (int(input(f'Enter the number of seats sold in section A: ')))
    seatsB = (int(input(f'Enter the number of seats sold in section B: ')))
    seatsC = (int(input(f'Enter the number of seats sold in section C: ')))
  
    ticketsSold = seatsA + seatsB + seatsC
    return seatsA, seatsB, seatsC, ticketsSold

def price(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC):
    income = (seatsA * sectionA) + (seatsB * sectionB) + (seatsC * sectionC)
    return income

def receipt(seatsA, seatsB, seatsC, sectionA, sectionB, sectionC, ticketsSold, income):
    print(seatsA, 'seats sold in section A at $', sectionA, 'per ticket')
    print(seatsB, 'seats sold in section B at $', sectionB, 'per ticket')
    print(seatsC, 'seats sold in section C at $', sectionC, 'per ticket')
    print(f'The amount of tickets sold is: ', ticketsSold)
    print(f'The income is: ', income)
  
