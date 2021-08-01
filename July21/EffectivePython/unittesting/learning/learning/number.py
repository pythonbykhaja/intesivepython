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

        Raises:
          ValueError when number is less than zero
        """
        if self.__number < 0:
            raise ValueError("Number should be greater than zero")
        if self.__number == 0:
            return False
        return (self.__number%2 == 0)

    def factorial(self) -> int:
        """
        This method will calculate factorial

        Returns: factorial of a number 

        Raises:
          ValueError when number is less than zero
        """
        if self.__number < 0:
            raise ValueError("Number cannot be less than zero")
        return math.factorial(self.__number)
