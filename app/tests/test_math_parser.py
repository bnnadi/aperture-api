import unittest
import sympy as sp
from math_parser import MathParser

class TestMathParser(unittest.TestCase):

    def setUp(self):
        """Set up the MathParser instance before each test."""
        self.parser = MathParser()

    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        expression = "2 + 3 * 4"
        result = self.parser.parse_expression(expression)
        self.assertEqual(result, 14)

    def test_exponentiation(self):
        """Test exponentiation."""
        expression = "2^3 + 4^2"
        result = self.parser.parse_expression(expression)
        self.assertEqual(result, 24)

    def test_parentheses(self):
        """Test parentheses handling."""
        expression = "(2 + 3) * (4 - 2)"
        result = self.parser.parse_expression(expression)
        self.assertEqual(result, 10)

    def test_trigonometric_function(self):
        """Test trigonometric functions."""
        expression = "sin(pi / 2)"
        result = self.parser.parse_expression(expression, substitutions={'pi': sp.pi})
        self.assertAlmostEqual(result, 1.0)

    def test_logarithm(self):
        """Test logarithmic functions."""
        expression = "log(100)"
        result = self.parser.parse_expression(expression)
        self.assertAlmostEqual(result, sp.log(100).evalf())

    def test_variable_expression(self):
        """Test expressions with variables."""
        expression = "x^2 + 2*x + 1"
        result = self.parser.parse_expression(expression)
        expected = sp.sympify("x^2 + 2*x + 1")
        self.assertEqual(result, expected)

    def test_variable_substitution(self):
        """Test variable substitution in an expression."""
        expression = "x^2 + 2*x + 1"
        substitutions = {'x': 5}
        result = self.parser.parse_expression(expression, substitutions=substitutions)
        self.assertEqual(result, 36)

    def test_integration(self):
        """Test integration of a function."""
        expression = "x^2"
        result = self.parser.integrate(expression, 'x')
        expected = sp.integrate(sp.sympify(expression), sp.Symbol('x'))
        self.assertEqual(result, expected)

    def test_differentiation(self):
        """Test differentiation of a function."""
        expression = "sin(x)"
        result = self.parser.differentiate(expression, 'x')
        expected = sp.diff(sp.sympify(expression), sp.Symbol('x'))
        self.assertEqual(result, expected)

    def test_euler_identity(self):
        """Test Euler's identity: e^(i*pi) + 1"""
        expression = "e^(i*pi) + 1"
        result = self.parser.parse_expression(expression, substitutions={'pi': sp.pi, 'e': sp.E, 'i': sp.I})
        self.assertAlmostEqual(result, 0)

if __name__ == "__main__":
    unittest.main()