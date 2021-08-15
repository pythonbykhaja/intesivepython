import datetime

def document(func):
    """This function is a decorated to document the functions getting called
    """
    def document_function(*args, **kwargs):
        print(f"Running Function: {func.__name__}")
        print(f"positional args: {args}")
        print(f"keyword args: {kwargs}")
        print(f"Execution Started @ {datetime.datetime.now()}")
        result = func(*args, **kwargs)
        print(f"Execution Completed @ {datetime.datetime.now()}")
        return result
    return document_function


def is_prime(number):
    for index in range(2, number//2+1):
        if number%index == 0:
            return False
    return True

@document
def sum_of_prime_numbers(max):
    numbers = list(range(2,max+1))
    prime_numbers = list(filter(is_prime, numbers))
    return sum(prime_numbers)

if __name__ == "__main__":
    print(sum_of_prime_numbers(10))