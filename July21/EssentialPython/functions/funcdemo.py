
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


# https://projecteuler.net/problem=10

sum = 0
max_number = 2000000 
print("Calculating prime numbers")
for index in range(2, max_number):
    print(index, end=',', sep='')
    if is_prime(index):
        sum += index
print()
print(f"sum of all prime numbers till {max_number} is {sum}")


    


