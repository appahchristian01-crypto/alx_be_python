from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # Create a list that holds different shapes
    shapes = [
        Rectangle(10, 5),  # Rectangle with length = 10 and width = 5
        Circle(7)          # Circle with radius = 7
    ]

    # Loop through each shape and print its area
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
