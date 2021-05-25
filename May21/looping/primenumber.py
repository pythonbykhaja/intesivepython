# This program will check whether the number is prime or not

number = int(input('Enter the number: '))
index = 2
is_prime = True # Flag approch
while index < number:
    if number % index == 0:
        # the number is divisible by index so not prime
        # should do some thing to specify number is not prime
        is_prime = False
        break
    index = index + 1

if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

