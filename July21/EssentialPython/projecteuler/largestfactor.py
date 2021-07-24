number = int(input('Enter the number: '))
# find the largest factor.
index = number - 1 
while index >= 2:
    if number % index == 0:
        print(index)
        break
    index -= 1
