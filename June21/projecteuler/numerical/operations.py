"""
This module performs some numerical operations
"""
import utils

def factors(number):
    values = []
    for index in utils.range_for_factors(number):
        if number%index == 0:
            values.append(index)
    return values

def factorial(number):
    value = 1
    for index in range(1, number+1):
        value *= index
    return value