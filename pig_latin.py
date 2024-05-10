# Pig Latin Translater
# Author: Branden Quach
# May 5, 2024
# Converts a phrase into the Pig Latin language.

# Main function
def main():
    # Prompt for phrase
    phrase = input(f'Enter a phrase to be translated: ')
    # Splits phrase into seperate words
    words = phrase.split()
    # Calls for the translation function for each word
    translated_words = (translator(word) for word in words)
    # Joins translated words together with spaces
    pig_latin_phrase = ' '.join(translated_words)
    # Prints translated phrase
    print(pig_latin_phrase)

# Translator function
def translator(word):
    # Signifies vowels to be checked for
    vowels = 'aeiou'
    # Checks if first character of word is a vowel
    if word[0].lower() in vowels:
        # Returns word with 'ay' at the end
        return word + 'ay'
    else:
        # Returns word with first character at the end and adds 'ay'
        return word[1:] + word[0] + 'ay'
# Calls main function
main()
