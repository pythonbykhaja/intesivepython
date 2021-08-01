"""This module has functions for basic geometric caclulations

In this module we will have two classes Circle and Rectangle

Usage:
  circle = Circle(radius = 10)
  circle.area()

  rectangle = Rectangle(length=10, breadth=15)
  rectangle.area()
  rectangle.perimeter()
"""

class Circle:
    """ This class represents the circle

    Attributes:
      radius: This represents the radius of the circle
    """
    def __init__(self, radius):
        """Initializes the Circle Object

        Arguments:
          radius (float): radius of the circle
        """
        self.radius = radius

    def area(self):
        """This instance method will calculate area of circle

        Returns:
           A float representing area of circle
        """
        return 3.14 * self.radius ** 2
        