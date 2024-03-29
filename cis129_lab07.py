# Lab 7: The Dice Game
# Author: Branden Quach
# March 29, 2024
# Two player dice game

# Libraries
import random

# Main function
def main():
    print()

    # Variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    while endProgram == 'no':

        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0

        winnerName = rolldice(p1number, p2number, playerOne, playerTwo, winnerName)
        
        print(f'The winner is: ', winnerName)
        endProgram = input(f'Do you want to end the program? (yes/no): ')

# Player names
def inputNames(playerOne, playerTwo):
    playerOne = input(f'Enter name for Player One: ')
    playerTwo = input(f'Enter name for Player Two: ')
    return playerOne, playerTwo

# Random numbers
def rolldice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    # Winners
    if p1number > p2number:
        return playerOne
    elif p2number > p1number:
        return playerTwo
    else:
        return 'TIE'
    
main()
