class Number:
    """This class has mathematical functions of number
    """
    def __init__(self, number:int) -> None:
        """Initialization with number
        """
        self.number = number

    def is_prime(self):
        """This method will find if the number is prime or not
        """
        if self.number <= 1:
            return False
        for index in range(2, self.number//2 +1):
            if self.number%index == 0:
                return False
        return True

    def is_even(self):
        """This method will find if the number is even or not
        """
        if self.number <= 0:
            return False
        return self.number%2 == 0


class AdvancedNumber(Number):
    pass
