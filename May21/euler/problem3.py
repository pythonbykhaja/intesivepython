# This program solves the project euler problem 3
# https://projecteuler.net/problem=3

# This program attempts to find the largest prime factor
number = int(input('Enter the number to calculate largest prime factor: '))

index = number // 2
while index >= 2:
    if number % index == 0:
        # index is a factor
        # we need to check if index is prime
        prime_index = 2
        while prime_index <= (index //2):
            if index % prime_index == 0:
                # not a prime
                break
            prime_index += 1
        else:
            print(f"{index} is largest prime factor")
            break
    index -= 1
else:
    print(f'The {number} has no prime factors ')