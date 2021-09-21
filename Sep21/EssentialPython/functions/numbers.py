def is_prime(number):
    """
    This function finds if the number is prime or not
    """
    for index in range(2, number//2 + 1):
        if number%index == 0:
            return False
    return True


# printing prime numbers between 10-20
for number in range(10,21):
    if is_prime(number):
        print(number)

# list of all prime numbers b/w 100 to 1000
prime_numbers = [number for number in range(10,1001) if is_prime(number)]
print(prime_numbers)

