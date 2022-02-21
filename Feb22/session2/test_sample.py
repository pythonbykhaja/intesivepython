from sample import add

def test_add_numbers():
    """
    This test method tests the add function with different number combinations
    """
    result = add(2,3)
    assert result == 5
    result = add(-1,1)
    assert result == 0