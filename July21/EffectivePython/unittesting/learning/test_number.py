from number import Number
def test_iseven_positive():
    number_1 = Number()
    number_2 = Number(10)
    number_3 = Number(11)
    assert(number_1.is_even() == False)
    assert(number_2.is_even() == True)
    assert(number_3.is_even() == False)
