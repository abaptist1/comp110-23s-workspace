# hello! this is a comment, NEEDS THE SPACE AFTER THE HASHTAG
"""DEmonstrates while loops by finding low value in string"""

cards: str = "5235"

card_index: int = 0
low_card: int = int(cards[0])

# look at each number (index) in the string
while card_index < 4:
    #check if current card is less then low card
    current_card: int = int(cards[card_index])
    if (current_card < low_card):
        #update the low card to be the value of our current card
        low_card = current_card
    card_index = card_index + 1
print(low_card)