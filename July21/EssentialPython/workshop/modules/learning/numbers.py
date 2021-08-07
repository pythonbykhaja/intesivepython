"""This module has reusable functions for numeric opertations
"""

def factors(number: int) -> list:
    """This method will return the factors of the number 

    Returns:
       A list of factors for the number
    """
    factors_found = list()
    for index in range(2, number):
        if number%index == 0:
            factors_found.append(index)
    return factors_found

def is_prime(number: int) -> bool:
    """This method will find if the number is prime or not

    Returns: True if prime False otherwise
    """
    factors_number = factors(number)
    if len(factors_number) == 0:
        return True
    return False

pi = 3.14