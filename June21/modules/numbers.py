def is_prime(number):
    """
    This function will help in finding whether the number is prime or not
    """
    for index in range(2,(number//2)+1):
        if number%index == 0:
            return False
    return True

def factors(number):
    """
    This method will return the factors
    """
    values = []
    for index in range(2,(number//2)+1):
        if number%index == 0:
            values.append(index)

    return values

if __name__ == '__main__':
    # This code will be execute when the program is execute as python numbers.py
    print(factors(6))
    print(is_prime(70))