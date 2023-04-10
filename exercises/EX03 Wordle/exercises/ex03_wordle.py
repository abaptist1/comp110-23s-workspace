""" Exercise 03 Wordle! """

__author__ = "730473328"

# Part 4 goes here at the top need to use f strings for the text that displays how many tries the user has made

def contains_char(guess: str, char: str) -> bool:
    """Returns True if char matchaes any of the indeses of the guess string, False if not"""
    search_index: int = 0
    assert len(char) == 1
    while search_index < len(guess):
        if guess[search_index] == char:
            return True
        search_index = search_index + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Turns guess into string of emojis depending on what indexes match the secret word"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_result: str = ""
    search_index = 0
    contains: bool = False
    assert len(guess) == len(secret)
    while search_index < len(secret):
        if guess[search_index] == secret[search_index]:
            emoji_result = emoji_result + GREEN_BOX
        else:
            contains = contains_char(secret, guess[search_index])
            if contains:
                emoji_result = emoji_result + YELLOW_BOX
            else:
                emoji_result = emoji_result + WHITE_BOX
        search_index = search_index + 1
    return emoji_result

def input_guess (expected_length: int) -> str:
    """Determines if the lenght of the guess matches the expected length"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
       guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn_number: int = 1
    game_result: bool = False
    guess: str = ""
    while turn_number <= 6 and game_result == False:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(5)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turn_number}/6 turns!")
            game_result = True
        turn_number = turn_number + 1
    if turn_number > 6:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()