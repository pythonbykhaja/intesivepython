number = int(input('Enter the number: '))
# Find the largest prime factor
factor = number//2 
while factor >= 2:
    if number%factor == 0:
        # This is largest factor
        # Need to check if factor is prime or not
        index = 2
        while index <= factor//2:
            if factor % index == 0:
                break
            index += 1
        else:
            print(factor)
            break
    factor -= 1