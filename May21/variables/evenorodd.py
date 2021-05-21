# This programs accepts a integer as an input and determines
# if the number is even or odd
number = int(input('Enter the number: '))
remainder = number % 2
if remainder == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")