# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform an arithmetic operation (add, subtract, multiply, divide).
    Returns a number for valid operations or an error message string.
    """
    op = str(operation).strip().lower()

    try:
        a = float(num1)
        b = float(num2)
    except (ValueError, TypeError):
        return "Error: Non-numeric input"

    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operation. Use add, subtract, multiply, or divide."
