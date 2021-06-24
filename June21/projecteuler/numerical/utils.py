"""
This module has utility functions
"""

def half_number(number):
    """
    half the number for range functions
    """
    return (number//2 + 1)

def range_for_factors(number):
    max = half_number(number)
    return range(2, max)