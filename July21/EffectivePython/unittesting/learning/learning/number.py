import math

class Number:
    def __init__(self, number=0) -> None:
        """Initalization of the number class
        Args:
          number (int) Represents a Number
        """
        self.__number = number

    def is_even(self) -> bool:
        """
        This method will check if the number is even or not

        Returns: True if even false otherwise
        """
        if self.__number == 0:
            return False
        return (self.__number%2 == 0)

    def factorial(self) -> int:
        """
        This method will calculate factorial

        Returns: factorial of a number 
        """
        return math.factorial(self.__number)
