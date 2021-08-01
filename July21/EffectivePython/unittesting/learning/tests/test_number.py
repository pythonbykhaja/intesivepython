from learning.number import Number
import pytest

def test_iseven_positive():
    number_1 = Number()
    number_2 = Number(10)
    number_3 = Number(11)
    assert(number_1.is_even() == False)
    assert(number_2.is_even() == True)
    assert(number_3.is_even() == False)


def test_iseven_negative():
    number_1 = Number(-2)
    with pytest.raises(ValueError):
        number_1.is_even()

