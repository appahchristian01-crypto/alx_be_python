# test_arithmetic.py
from arithmetic_operations import perform_operation

cases = [
    (5, 6, "add"),
    (10, 0, "divide"),
    (7, 3, "subtract"),
    (2, 4, "multiply"),
    ("abc", 2, "add"),
    (2, 3, "power"),
]

for a, b, op in cases:
    result = perform_operation(a, b, op)
    print(f"{a} {op} {b} -> {result}")
