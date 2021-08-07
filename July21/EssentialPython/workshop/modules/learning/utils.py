"""This module has utilities
"""

def collect_number_input(count=1):
    """
    This method will collect the number inputs
    """
    index = 0
    numbers = []
    while index < count:
        numbers.append(int(input(f'Enter the number {index+1}: ')))
        index += 1
    return numbers
        