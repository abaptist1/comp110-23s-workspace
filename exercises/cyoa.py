"""Exercise 06 Choose your own Adventure, Coin Gambling."""
from random import randint


__author__ = "730473328"

COIN_EMOJI: str = "\U00000000"
player: str = ""
points: int = 5


def greet() -> None:
    """Greets player."""
    COIN_EMOJI: str = "\U0001FA99"
    print(f"Hi there! Welcome to Coin {COIN_EMOJI} Gambling. Test your luck and confidence! Guess the result of the flip right and get 10 points! Think you can get two right in one guess? DOUBLE ALL YOUR POINTS or lose risked points if you're wrong!")
    global player
    player = input("Enter ya name here cheif: ")


def option_a() -> None:
    """Custom procedure to flip coin once."""
    # Custom Procedure
    global points
    COIN_EMOJI = "\U0001FA99"
    start_option_input = input(f"Now you'll flip a coin once and if you get it right you get a point. input 1 for Heads, 2 for Tails Ready to go? {COIN_EMOJI} Yes/No: ")
    if start_option_input == "Yes":
        coin_result = randint(1, 2)
        player_response = int(input("Heads (1) or Tails(2)?: "))
        if player_response == coin_result:
            points += 10
            print(f"Nice one! you earned 1 point! Total points: {points}")
        else:
            print(f"Wrong! Total points: {points}") 
        return None
    else:
        return None


def option_b(points: int) -> int:
    """Option of gambling points for a chance at doubling points!"""
    # Custom function
    global player
    points_risked = int(input(f"How many points out of your total of {points} would you like to gamble?: "))
    print(f"Alright {player}. Lets go!")
    coin_flip_result_1 = randint(1, 2)
    coin_flip_result_2 = randint(1, 2)
    player_response_1 = input(f"Whats your first guess {player}?: ")
    player_response_2 = input("Second guess?: ")
    if int(player_response_1) == coin_flip_result_1 and int(player_response_2) == coin_flip_result_2:
        points = points * 2
        print(f"Congrats {player} you now have a total of {points} points.")
    else:
        points = points - points_risked
        print(f"Sorry! better luck next time {player} you now have {points} points.")
    return points


def option_c() -> None:
    """Exits the game."""
    global points
    print(f"Sorry to see you go {player} you got a total of {points} points. Thanks for playing!")


def main() -> None:
    """Main function that runs the coin flip game."""
    greet()
    print(f"How would you like to proceed {player}? Please enter the letter of your choice.")
    print("A. Flip a coin once")
    print("B. Flip a coin twice and get both right for double points but risk losing a point!")
    print("C. Exit the game")
    player_choice: str = input("Enter letter here: ")
    while player_choice != "C":
        if player_choice == "A":
            option_a()
        if player_choice == "B":
            option_b(points)
        print(f"How would you like to proceed {player}? Please enter the letter of your choice.")
        print("A. Flip a coin once")
        print("B. Flip a coin twice and get both right for double points but risk losing a point!")
        print("C. Exit the game")
        player_choice = input("Enter letter here: ")
    if player_choice == "C":
        option_c()


if __name__ == "__main__":
    main()