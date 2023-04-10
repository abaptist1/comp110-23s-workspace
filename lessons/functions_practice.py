"""Practice Writing Functions"""

# Using def to define a function
def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

mimic("Hello!")

print(mimic("Hello!"))


# Second way to write the function
my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)