class Student:
    def __init__(self,name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value



class Circle():
    def __init__(self, radius) -> None:
        self.__radius = radius

    @property
    def diameter(self):
        return 2 * self.__radius

    @property
    def area(self):
        import math
        return math.pi * self.__radius ** 2
        

s1 = Student('Ram')
print(s1.name)
s1.name = "Shyam"
print(s1.name)

c1 = Circle(10)
print(c1.diameter)
print(c1.area)

