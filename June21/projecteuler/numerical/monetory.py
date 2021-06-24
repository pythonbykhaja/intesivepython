"""
This module implements the monetory numerical calculations
"""

def simple_interest(principal, time, rate):
    return (principal * time * rate / 100)

def compound_interest(principal, time, rate):
    return principal * (( 1 + (rate/100)) ** time)