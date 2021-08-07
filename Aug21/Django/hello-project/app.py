"""This module is for learning

This module has basic functions to work with numbers

"""


def is_even(number: int) -> bool:
    """
    This method will find if the number passed is even or not
    :param number : a number
    :return: True if even False otherwise
    """
    if number <= 0:
        return False
    return number % 2 == 0

print(__name__)

if __name__ == '__main__':
    # if someone is executing the code directly  by calling python app.py then this block will be executed
    print(is_even(5))
    print(is_even(10))
