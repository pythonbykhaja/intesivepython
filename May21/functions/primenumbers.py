def is_prime(number):
    """
    This function will check if the number is prime or not

    returns True if prime false otherwise
    """
    for index in range(2, number//2):
        if number%index == 0:
            return False
    return True

prime_count = 0
number = 1
while (prime_count < 10001):
    number += 1
    if is_prime(number):
        prime_count +=1
 
# Print answer
print(number)