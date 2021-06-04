## Problem 1: Number Guessing Game
* Write a function called as guessing_game that takes no arguments
* When run the function chooses a random integer between 0 and 100
* Then ask the user to guess a number
* Each time user enters guess, the program indicates one of the following
  * Too high
  * Too Low
  * Just right
* If the user guesses correctly the program exits, Otherwise, the user is asked to try again
* To guess the random number between 0 and 100 use the following code
```python
import random
number = random.randint(0,100)
```

## Problem 2: Pig Latin
* This is common children's secret language.
  * If the word begins with vowel (a,e,i,o,u), add "way" to the end
    * Example: air => airway, apple => appleway
  * If the word begins with any other character, then we take the first letter and put it on the end of the word add "ay"
    * Example: python => ythonpay, laptop => aptoplay
* Write a function called as pig_latin that takes string as a input and returns the translation of this word to pig latin