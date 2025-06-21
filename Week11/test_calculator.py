import unittest
import math
from calculator import add, subtract, multiply, divide, power, root, sine, cosine, tangent

class TestCalculator(unittest.TestCase):

    # Basic Arithmetic operations (add,subtract,multiply,divide)
    def test_add(self):
        self.assertEqual(add(45, 30), 75)
        self.assertEqual(add(-5, 5), 0)

    def test_subtract(self):
        self.assertEqual(subtract(15, 3), 12)
        self.assertEqual(subtract(43, 55), -12)

    def test_multiply(self):
        self.assertEqual(multiply(4, 2), 8)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 1 / 3)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    # Advanced Mathematics (power, root)
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(9, 0.5), 3)

    def test_root(self):
        self.assertEqual(root(36, 2), 6)
        self.assertEqual(root(-27, 3), -3)
        with self.assertRaises(ValueError):
            root(-16, 2)

    # Trigonometric Functions (sine, cosine, tangent)
    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0.0)
        self.assertAlmostEqual(sine(90), 1.0)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1.0)
        self.assertAlmostEqual(cosine(180), -1.0)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(45), 1.0)
        self.assertAlmostEqual(tangent(0), 0.0)
        with self.assertRaises(ValueError):
            tangent(90)  # Undefined

    # Input validation and edge cases
    def test_edge_cases(self):
        self.assertEqual(power(0, 0), 1)  # By convention
        self.assertEqual(root(0, 2), 0)

if __name__ == '__main__':
    unittest.main()