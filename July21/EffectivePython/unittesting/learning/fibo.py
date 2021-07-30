
def fibonacci(index: int) -> int:
    """
    This function will return the fibonacci series number 

    Args:
       index(int): index of the fibonacci series

    Return:
        number based on the index pass

    """
    if index == 0:
        return 0
    elif index == 1:
        return 1
    first = 0
    second = 1
    count = 1
    value = 0
    while count < index:
        value = first + second
        first = second
        second = value
        count += 1
    return value


if __name__ == '__main__':
    fibonacci(2)
