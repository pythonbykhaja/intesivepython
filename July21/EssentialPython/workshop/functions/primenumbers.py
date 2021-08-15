def is_prime(number):
    for index in range(2, number//2 + 1):
        if number%index == 0:
            return False
    return True


def prime_numbers(start=2, end=100):
    for number in range(start, end+1):
        if is_prime(number):
            yield number

if __name__ == '__main__':
    for prime in prime_numbers(100,120):
        print(prime)