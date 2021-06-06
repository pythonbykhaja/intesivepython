def factorial(number):
    """
    This method calculates the factorial of the number
    """
    result = 1
    for index in range(1,number+1):
        result *= index
    return result

def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number-1)

print(factorial(5))
print(fact(5))