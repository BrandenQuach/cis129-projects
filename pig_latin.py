# Pig Latin Translater
# Author: Branden Quach
# May 5, 2024
# Converts a phrase into the Pig Latin language.

def main():
    phrase = input(f'Enter a phrase to be translated: ')
    words = phrase.split()
    translated_words = (translator(word) for word in words)
    pig_latin_phrase = ' '.join(translated_words)
    print(pig_latin_phrase)
  
def translator(word):
    vowels = 'aeiou'
    if word[0].lower() in vowels:
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'
main()
