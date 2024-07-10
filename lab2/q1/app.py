from classes.circle import Circle
from classes.square import Square
from classes.rectangle import Rectangle

circle = Circle("Circle", "red", 7)
square = Square("Square", "yellow", 8)
rectangle = Rectangle("Rectangle", "green", 5, 5)

print("Area of Circle:", circle.calculate_area())
print("Area of Square:", square.calculate_area())
print("Area of Rectangle:", rectangle.calculate_area())
