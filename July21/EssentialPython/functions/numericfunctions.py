def is_even(number:int):
    """
    This function verifies if the number is even or not

    Returns:
        True if even false other wise
    """
    return number % 2 == 0

def is_prime(number: int):
    """
    This function finds if the number is prime
    Returns:
        True if prime false otherwise
    """
    for index in range(2, (number//2) + 1):
        if number%index == 0:
            return False
    return True

def factorial(number: int):
    """
    This function calculates the factorial of a number
    """
    result = 1
    for index in range(1,number+1):
        result *= index
    return result

def simple_interest(principal: float, rate: float, time: int):
    """
    This function will calculate the simple interest
    """
    return (principal * time * rate / 100)

def compound_interest(principal: float, rate: float, time: int):
    pass

