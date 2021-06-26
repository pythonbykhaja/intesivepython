def is_prime(number):
    """
    This function calculates if the number is prime or not

    Args: 
        number(int): Number to check for prime

    Returns:
        bool: True if prime False otherwise

    Raises:
        ValueError: Value Error is raised when the argument to this function is 
        not an integer or integer with less than 2 as value

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if not isinstance(number, int):
        raise ValueError('number should be of type int')
    if number< 2:
        raise ValueError('number should be greater than or equal 2')
    for index in range(2, number//2 + 1):
        if number%index == 0:
            return False
    return True


if __name__ == '__main__':
    while True:
        try:
            number = int(input('Enter the number: '))
            if is_prime(number):
                print(f"{number} is prime")
            
            choice = input('Do you want to continue: y or n ')
            if choice == 'n':
                break
        except ValueError as ve:
            print(ve)