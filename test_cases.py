import unittest
import math

from calculator import *

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(5, -3), -15)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), "Error: Division by zero")
        self.assertEqual(divide(-10, 2), -5)

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(-1), "Error: Cannot calculate square root of a negative number")

    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(3, 2), 9)
        self.assertEqual(exponentiation(5, 0), 1)

    def test_sine(self):
        self.assertAlmostEqual(sine(30), 0.5, places=2)
        self.assertAlmostEqual(sine(45), math.sqrt(2) / 2, places=2)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(60), 0.5, places=2)
        self.assertAlmostEqual(cosine(45), math.sqrt(2) / 2, places=2)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(45), 1.0, places=2)
        self.assertAlmostEqual(tangent(30), 0.577, places=2)

    def test_logarithm(self):
        expected_result = 2.302585092994046  # Expected result with higher precision
        self.assertAlmostEqual(logarithm(10), expected_result, places=3)


    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_absolute_value(self):
        self.assertEqual(absolute_value(5), 5)
        self.assertEqual(absolute_value(-5), 5)

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(0, 5), 5)

    def test_lcm(self):
        self.assertEqual(lcm(48, 18), 144)
        self.assertEqual(lcm(0, 5), 0)

    def test_arc_sine(self):
        self.assertAlmostEqual(arc_sine(0.5), 30.0, places=1)
        self.assertAlmostEqual(arc_sine(1), 90.0, places=1)

    def test_arc_cosine(self):
        self.assertAlmostEqual(arc_cosine(0.5), 60.0, places=1)
        self.assertAlmostEqual(arc_cosine(1), 0.0, places=1)

    def test_arc_tangent(self):
        self.assertAlmostEqual(arc_tangent(1), 45.0, places=1)
        self.assertAlmostEqual(arc_tangent(0.577), 30.0, places=1)

    def test_hyperbolic_sine(self):
        self.assertAlmostEqual(hyperbolic_sine(0), 0.0, places=2)
        self.assertAlmostEqual(hyperbolic_sine(1), 1.175, places=2)

    def test_hyperbolic_cosine(self):
        self.assertAlmostEqual(hyperbolic_cosine(0), 1.0, places=2)
        self.assertAlmostEqual(hyperbolic_cosine(1), 1.543, places=2)

    def test_hyperbolic_tangent(self):
        self.assertAlmostEqual(hyperbolic_tangent(0), 0.0, places=2)
        self.assertAlmostEqual(hyperbolic_tangent(1), 0.761, places=2)

    def test_ceil(self):
        self.assertEqual(ceil(4.2), 5)
        self.assertEqual(ceil(-4.2), -4)

    def test_floor(self):
        self.assertEqual(floor(4.7), 4)
        self.assertEqual(floor(-4.7), -5)

    def test_round_to_nearest(self):
        self.assertEqual(round_to_nearest(4.2), 4)
        self.assertEqual(round_to_nearest(4.7), 5)

if __name__ == "__main__":
    unittest.main()
