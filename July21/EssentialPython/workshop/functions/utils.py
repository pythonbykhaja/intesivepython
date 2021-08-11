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

def convert_curreny(amount, **kwargs):
    """This function converts from one currency to other
    """
    #amount = kwargs['amount']
    source = kwargs['source']
    destination = kwargs['destination']
    rate = kwargs['rate']
    target = amount * rate
    return target

def is_leap(year):
    """This function finds if the year passed is leap or not
    Arguments:
      year (int): year 

    Return: True if leap false other wise
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    convert_curreny(source='usd', destination='inr', amount=135, rate=74.5)