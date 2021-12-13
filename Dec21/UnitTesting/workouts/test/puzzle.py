import random

def guessing_game() -> int:
    """
    This function should guess a number between 0 and 100
    """
    return random.randint(0, 100)

def pig_latin(word: str) -> str:
    """
    This method will return the pig_latin 

    if the word begins with vowel (a, e, i, o, u) add "way" at the end of the word
    if the word begins with any other letter, 
    then we take the first letter and put it on the end and add `ay`


    Examples
    1. air => airway
    2. computer => omputercay
    3. python => ythonpay
    """
    if len(word) == 0:
        return ''
        
    if word[0] in 'aeiou':
        return f"{word}way"

    return f"{word[1:]}{word[0]}ay"
