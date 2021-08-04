def is_prime(number):
    for index in range(2, number):
        if number%index == 0:
            return False
    
    return True


print(is_prime(9))