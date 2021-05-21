# This program takes length and breadth as input from users &
# Calculates area of rectangle and perimeter of rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area of the rectangle is {area}")
print(f"Perimeter of the rectangle is {perimeter}")