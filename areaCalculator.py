import math


def triangleArea(base, height):
    return 0.5 * base * height


def squareArea(side):
    return side**2


def rectangleArea(width, length):
    return width * length


def circleArea(radius):
    return math.pi * radius**2


# Get user input for triangle dimensions
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print("The area of the triangle is:", triangleArea(base, height))

# Get user input for square side
side = float(input("Enter the side length of the square: "))
print("The area of the square is:", squareArea(side))

# Get user input for rectangle dimensions
width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))
print("The area of the rectangle is:", rectangleArea(width, length))

# Get user input for circle radius
radius = float(input("Enter the radius of the circle: "))
print("The area of the circle is:", circleArea(radius))
