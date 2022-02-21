from email.utils import formataddr
from picnic import food_items

def test_food_items():
    """
    This test case will test the food_items function
    """
    result = food_items('salad')
    assert result == "You are bringing salad"
    result = food_items('salad', 'chips')
    assert result == "You are bringing salad and chips"
    result = food_items('salad', 'chips', 'cake')
    assert result == "You are bringing salad, chips and cake"
    result = food_items('salad','muffins', 'chips', 'cake')
    assert result == "You are bringing salad, muffins, chips and cake"
    result = food_items('salad','icecream', 'muffins', 'chips', 'cake')
    assert result == "You are bringing salad, icecream, muffins, chips and cake"
    result = food_items()
    assert result == ""