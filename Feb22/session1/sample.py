def add(number_1, number_2):
    """Adds two numbers

    Args:
      number_1: This is the first number
      number_2: This is the second number

    Returns:
      sum of two arguments passed 
    
    """
    return number_1 + number_2

if __name__ == "__main__":
    num_1 = 10
    num_2 = 20
    result = add(num_1, num_2)
    # Lets change the output to something like 10 + 20 => 30
    print(f"{num_1} + {num_2} => {result} ")