import math
class Point:
    """
    Represents the two-dimensional  geometric co-ordinate
    >>> p_0 = Point()
    >>> p_1 = Point(3,5)
    """
    def __init__(self, x: float = 0, y:float =0) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        This instance method resets the geometric co-ordinates back to origin
        """
        self.x = 0
        self.y = 0

    def distance(self, other: "Point") -> float:
        """
        Calculate the Euclidean distance between two points
        """
        #math.hypot(self.x - other.x, self.y-other.y)
        return math.sqrt((self.x - other.x)**2 + (self.y -other.y)**2)
    
    def move(self, x: float, y: float) -> None:
        """
        This method moves the point to the new location in 2D space
        """
        self.x += x
        self.y += y

    def print_location(self) -> str:
        return f"({self.x}, {self.y})"



class Point3D(Point):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x=x, y=y)
        self.z = z

    def print_location(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def reset(self) -> None:
        super().reset()
        self.z = 0

    def move(self, x: float, y: float, z: float) -> None:
        super().move(x, y)
        self.z += z

    def distance(self, other: "Point3D") -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y -other.y)**2 + (self.z - other.z)**2)

