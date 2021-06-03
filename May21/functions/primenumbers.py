def is_prime(number):
    """
    This function will check if the number is prime or not

    returns True if prime false otherwise
    """
    
    for index in range(2, number//2):
        if number%index == 0:
            return False
    return True
    
min = 100
max = 1000
for number in range(min,max+1):
    if is_prime(number):
        print(number)