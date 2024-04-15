# Lab 8: Palindrome Tester
# Author: Branden Quach
# April 13, 2024
# Checks if input is a palindrome or not

# Constant variables
stack = []
top = -1

# Main function
def main():
    # Calls function for user input
    getWord = getValidWord()
    # Removes spaces and lowercases input
    lowerWord = getWord.replace(' ', '').lower()
    # Ignores special characters
    word = ''.join(characters for characters in lowerWord if characters.isalnum())
    # Calls palindrome function for a true or false output
    if isPalindrome(word):
        print(f'True, {getWord} is a palindrome!')
    else:
        print(f'False, {getWord} is not a palindrome.')
        
# Function to receive input from user
def getValidWord():
    # User prompt
    getWord = input('Enter a word: ')
    # Checks for integers within input
    if any(characters.isdigit() for characters in getWord):
        print(f'{getWord} is not a valid word. Please try again.')
        return getValidWord()
    else:
        return str(getWord)

# Function to check if input is a palindrome
def isPalindrome(word: str) -> bool:
    # Allows data transfer for stack variable
    global stack
    # Calculates word length
    wordLength = len(word)
    # Creates a stack according to word length
    stack = ['0'] * (wordLength +1)
    # Finds the middle of word
    mid = wordLength // 2
    i = 0
    # Omits middle letter for odd number of letter words
    while i < mid:
        pushWord(word[i])
        i += 1
    if wordLength % 2 != 0:
        i += 1
    # Checks if letters are the same from front and back
    while i < wordLength:
        character = popWord()
        if character != word[i]:
            return False
        i += 1
    return True

# Removes character from the top of stack
def popWord():
    global top
    character = stack[top]
    top -= 1
    return character
    
# Adds character to the top of stack
def pushWord(character: str):
    global top
    top += 1
    stack[top] = character
    
# Calls main function
main()
