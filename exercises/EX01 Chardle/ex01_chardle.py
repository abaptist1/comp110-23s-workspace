"""EX 01 - Chardle - A Cute Step Toward Wordle."""

__author__ = "730473328"

# """Asking for inputs and checking for errors"""
five_letter_word: str = input("Enter a 5-character word: ")
five_letter_word_count: int = len(five_letter_word)
if (five_letter_word_count > 5):
    print("Error: Word must contain 5 characters")
    exit()
if (five_letter_word_count < 5):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
character_count: int = len(character)
if (character_count > 1):
    print("Error: Character must be a single character.")
    exit()
if (character_count == 0):
    print("Error: Character must be a single character.")
    exit()
    
x: int = 0

# """Checking Indicies for Matches"""
print("Searching for " + character + " in " + five_letter_word)

if (five_letter_word[0] == (character)):
    print(character + " found at index 0")
    x = x + 1
if (five_letter_word[1] == (character)):
    print(character + " found at index 1")
    x = x + 1
if (five_letter_word[2] == (character)):
    print(character + " found at index 2")
    x = x + 1
if (five_letter_word[3] == (character)):
    print(character + " found at index 3")
    x = x + 1
if (five_letter_word[4] == (character)):
    print(character + " found at index 4")
    x = x + 1

# """Counting instances of characters"""
if (x == 0):
    print("No instances of " + character + " found in " + five_letter_word) 

if (x == 1):
    print(str(x) + " instance of " + character + " found in " + five_letter_word)

if (x > 1):
    print(str(x) + " instances of " + character + " found in " + five_letter_word)
