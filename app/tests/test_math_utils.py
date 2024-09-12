import unittest
from utils.math_utils import expression_to_latex

class TestMathUtils(unittest.TestCase):

    def test_expression_to_latex(self):
        self.assertEqual(expression_to_latex("x^2 + y^2"), "x^{2} + y^{2}")
        self.assertEqual(expression_to_latex("sin(x)"), "\\sin{\\left(x \\right)}")
        self.assertTrue("Error" in expression_to_latex("invalid_expression"))

if __name__ == '__main__':
    unittest.main()
