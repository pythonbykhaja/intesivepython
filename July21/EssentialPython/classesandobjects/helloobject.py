class Number:
    """
    This class represents a number
    """
    def __init__(self, number: int) -> None:
        self.number = number
        

    def is_prime(self):
        """
        This method is used to find if the number is prime or Not
        """
        pass

    def is_even(self) -> bool:
        """
        This method is used to find if the number is even or not
        """
        return self.number%2 == 0

number1 = Number(4) #creating object or instantiation
number2 = Number(number=5) #creating object or instantiation

number1.is_even() # we write code using this
Number.is_even(number1) # This is how it actually gets called
