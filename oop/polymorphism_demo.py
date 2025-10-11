# polymorphism_demo.py
import math

class Shape:
    """A general shape. The area() method is a promise that child classes must keep."""
    def area(self):
        # This tells us: "You must override this in subclasses!"
        raise NotImplementedError("Subclasses must implement area()")

class Rectangle(Shape):
    """Rectangle with length and width."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # area of rectangle = length * width
        return self.length * self.width

class Circle(Shape):
    """Circle with radius."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # area of circle = π * radius^2
        return math.pi * (self.radius ** 2)


# Optional quick demo if you run this file directly:
if __name__ == "__main__":
    shapes = [Rectangle(10, 5), Circle(7)]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
