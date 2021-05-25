# This program will check whether the number is prime or not

number = int(input('Enter the number: '))
index = 2
while index < number:
    if number % index == 0:
        # the number is divisible by index so not prime
        # should do some thing to specify number is not prime
        print(f"{number} is not prime")
        break
    index = index + 1
else:
    # This code will be executed when the loop ended normally (no break call)
    print(f"{number} is prime")

print("Thanks for using my program")



