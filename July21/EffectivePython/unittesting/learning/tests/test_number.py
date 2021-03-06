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
    with pytest.raises(ValueError, match='Number should be greater than zero'):
        number_1.is_even()


def test_factorial_basic():
    number = Number(0)
    assert number.factorial() == 1

def test_factorial_exception():
    number = Number(-5)
    with pytest.raises(ValueError, match='Number cannot be less than zero'):
        number.factorial()


