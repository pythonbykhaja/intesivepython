"""This script will execute the learning application
"""
import messages
from numbers import is_prime, pi
from utils import collect_number_input as ni

if __name__ == "__main__":
    print(messages.welcome_message())

    number = int(input('Enter the number: '))
    if is_prime(number):
        print(f"{number} is prime")
    else:
        print(f"{number} is not a prime number")
    print(pi)

    numbers = ni(5)
