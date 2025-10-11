# class_static_methods_demo.py

class Calculator:
    # class attribute (shared by the whole class)
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: just adds two numbers, doesn't need the class or an object."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: has access to the class (cls) and its attributes."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Quick demo: run this file directly to see output
if __name__ == "__main__":
    # using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
