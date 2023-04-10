"""Second type of Mimic Function"""

def mimic_letter(my_words: str, letter_idx: int) -> str:
    if letter_idx >= len(my_words):
        return ("Too high of an index")
    else: 
        return (my_words[letter_idx])

print(mimic_letter("hello", 0))
    