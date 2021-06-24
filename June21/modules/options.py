import random

hotels = ['McDonalds', 'KFC', 'Burger King', 'Dominos', 'Pizza Hut', 'Shadab']

def pick_a_hotel():
    """
    This function picks a random hotel
    """
    return random.choice(hotels)