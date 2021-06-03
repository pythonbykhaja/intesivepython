def do_nothing():
    """
    This function does nothing
    """
    pass

def say_hello():
    """
    This function will say hello
    """
    print("hello")

def pi():
    """
    This function returns the pi value
    """
    return 3.14

def square(number):
    """
    This function returns the square of number

    paramters:
    number: 

    returns:
    square of number
    """
    return number ** 2

def power(number, index):
    """
    This function can calculate the power 
    """
    return number ** index

# calling function
say_hello()
do_nothing()
say_hello()
# Getting a return value from function
pi_value = pi()
print(pi_value)
print(square(10))
print(power(10,4))

