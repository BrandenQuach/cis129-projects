# Lab 8: Palindrome Tester
# Author: Branden Quach
# April 13, 2024
# Checks if input is a palindrome or not

stack = []
top = -1
# Main function
def main():
    word = getValidWord()

    if isPalindrome(word):
        print(f'{word} is a palindrome!')
    else:
        print(f'{word} is not a palindrome.')

def getValidWord():
    getWord = input('Enter a word: ')
    try:
        return str(getWord)
    except ValueError:
        print(f'{word} is not a valid word. Please try again.')
        return getValidWord()
def isPalindrome(word: str) -> bool:
    wordRefined = word.replace(' ', '').lower()
    wordLength = len(wordRefined)
    stack = ['0'] * (wordLength +1)
    mid = wordLength // 2
    i = 0
    while 1 < mid:
        push(wordRefined[i])
        i += 1
    if wordLength % 2 != 0:
        i += 1
    while i < wordLength:
        ele = pop()
        if ele != wordRefined[i]:
            return False
        i += 1
    return true
def pop():
    global top
    ele = stack[top]
    top -= 1
    return ele
def push(ele: str):
    global top
    top += 1
    stack[top] = ele
main()
