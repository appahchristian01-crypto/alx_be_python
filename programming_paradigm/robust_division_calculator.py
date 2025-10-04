# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Attempt to divide numerator by denominator.
    Returns:
      - "The result of the division is X" on success
      - "Error: Cannot divide by zero." if denominator is 0
      - "Error: Please enter numeric values only." if inputs are not numbers
    """
    # Try converting inputs to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Try dividing and catch division-by-zero
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
