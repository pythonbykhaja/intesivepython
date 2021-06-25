"""
This module implements functions which are used to query the numbers
"""
from . import utils

def is_prime(number):
    """
    This function checks the prime functionality
    returns: True if prime, False otherwise
    """
    for index in utils.range_for_factors(number):
        if number%index == 0:
            return False
    return True


def is_even(number):
    """
    This function checks the even functionality
    returns: True if even, False Otherwise
    """
    return (number%2 == 0)