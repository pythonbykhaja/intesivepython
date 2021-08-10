def product(*args):
    """This method returns the product of items passed as arguments

    Returns product of the arguments passed. If args length is zero then ti will return 0
    """
    if len(args) == 0:
        return 0

    result = 1
    for arg in args:
        result *= arg
    return result