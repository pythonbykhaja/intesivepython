from point import Point, Point3D

if __name__ == "__main__":
    p1 = Point(0,0)
    print(p1.print_location())
    p1.move(1,2)
    print(p1.print_location())
    p2 = Point(10,21)
    print(f"distance between p1 and p2 is {p2.distance(p1)}")

    p13d = Point3D(0,0,0)
    p13d.move(1,2,3) 
    print(p13d.print_location())

    p23d = Point3D(4,5,6)
    print(f"distance between p13d and p23d is {p23d.distance(p13d)}")



