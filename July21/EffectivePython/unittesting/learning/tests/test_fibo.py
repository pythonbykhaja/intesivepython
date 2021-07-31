from learning.fibo import fibonacci

def test_fibo_zero_index():
    """
    This test case will test fibonnaci zero index
    """
    assert fibonacci(0) == 0

def test_fibo_first_index():
    """
    This test case will test first index
    """
    assert fibonacci(1) == 1

def test_fibo_other_indexes():
    """
    This will test other indexes
    """
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2