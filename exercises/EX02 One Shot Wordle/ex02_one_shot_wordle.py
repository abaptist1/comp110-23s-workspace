"""EX02 One Shot Wordle!"""

__author__ = "730473328"

# Establishing a Secret and Prompting for a Guess

secret_word: str = "python"

six_letter_guess: str = input("What is your 6-letter guess? ")

while len(six_letter_guess) != len(secret_word):
    six_letter_guess = input("That was not 6-letters! Try again: ")
    
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Checking Indicies for correct matches
index_of_guess = 0
emoji_result = ""

while index_of_guess < len(secret_word):
    # Check if current inded of guessed word is equal to same index of secret word
    if six_letter_guess[index_of_guess] == secret_word[index_of_guess]:
        emoji_result = emoji_result + GREEN_BOX
    else:
        # Going to replace the white box code later put yellow box code here
        yellow: bool = False
        index_yellow: int = 0
        while not yellow and index_yellow < len(secret_word):
            if six_letter_guess[index_of_guess] == secret_word[index_yellow]:
                emoji_result = emoji_result + YELLOW_BOX 
                yellow = True
            index_yellow = index_yellow + 1
        if not yellow:
            emoji_result = emoji_result + WHITE_BOX
    index_of_guess = index_of_guess + 1
print(emoji_result)

if six_letter_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")