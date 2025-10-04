# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a fresh calculator before each test."""
        self.calc = SimpleCalculator()

    # ---------- add tests ----------
    def test_addition_basic(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_addition_more_cases(self):
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertEqual(self.calc.add(10**6, 1), 1000001)

    # ---------- subtract tests ----------
    def test_subtraction_basic(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_subtraction_decimal(self):
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3, places=7)

    # ---------- multiply tests ----------
    def test_multiplication_basic(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiplication_edge(self):
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    # ---------- divide tests ----------
    def test_division_basic(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_precision(self):
        # 1/3 is repeating, so use almost equal
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3, places=7)

    def test_divide_by_zero(self):
        # The calculator returns None when dividing by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
