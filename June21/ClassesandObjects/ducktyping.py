
class Shape():
    def area(self):
        return 0

    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        

    def area(self):
        return self.__breadth * self.__length


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        import math
        return math.pi * (self.__radius ** 2)

class Lion:
    def area(self):
        return "jungle"


def print_area(shape):
    print(f"area is {shape.area()}")

c1 = Circle(radius=1)
print_area(c1)

r1 = Rectangle(length=1, breadth=1)
print_area(r1)

l1 = Lion()
print_area(l1)
        


