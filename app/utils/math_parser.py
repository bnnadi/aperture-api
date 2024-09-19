import re
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

class MathParser:
    def __init__(self):
        self.transformations = standard_transformations + (implicit_multiplication_application,)
        self.symbols = {}
        self.defined_symbols(['x', 'y', 'z'])

    def defined_symbols(self, symbols):
        for symbol in symbols:
            self.symbols[symbol] = sp.Symbol(symbol)


    def parse_expression(self, expression: str, substitutions: bool = False):
        try:
            # Parse the expression into a SymPy expression
            parsed_expr = parse_expr(expression, transformations=self.transformations, local_dict=self.symbols)

            # Substitute variables if provided
            if substitutions:
                # Ensure substitutions use SymPy symbols
                subs = {self.symbols.get(k, sp.symbols(k)): v for k, v in substitutions.items()}
                parsed_expr = parsed_expr.subs(subs)

            # Evaluate the expression
            result = parsed_expr.evalf()

            return result
        except (SyntaxError, ValueError) as e:
            return ValueError(f"Error parsing expression: {e}")


    def differentiate(self, expression: str, variable: str):
        try:
            # Parse the expression into a SymPy expression
            parsed_expr = parse_expr(expression, transformations=self.transformations, local_dict=self.symbols)
            var = self.symbols.get(variable, sp.symbols(variable))
            # Differentiate with respect to the specified variable
            derivative = sp.diff(parsed_expr, var)

            return derivative
        except (SyntaxError, ValueError) as e:
            return ValueError(f"Error differentiating expression: {e}")

    def integrate(self, expression: str, variable: str):
        try:
            # Parse the expression into a SymPy expression
            parsed_expr = parse_expr(expression, transformations=self.transformations, local_dict=self.symbols)
            var = self.symbols.get(variable, sp.symbols(variable))
            # Integrate with respect to the specified variable
            integral = sp.integrate(parsed_expr, var)

            return integral
        except (SyntaxError, ValueError) as e:
            return ValueError(f"Error integrating expression: {e}")

if __name__ == "__main__":
    parser = MathParser()

    expresions = [
        "2 + 3 * 4",                # Basic arithmetic
        "2^3 + 4^2",                # Exponentiation
        "(2 + 3) * (4 - 2)",        # Parentheses
        "sin(pi / 2)",              # Trigonometric functions
        "log(100)",                 # Logarithms
        "e^(i*pi) + 1",             # Euler's identity
        "x^2 + 2*x + 1",            # Expression with variable
        "integrate(x^2, x)",        # Integration
        "diff(sin(x), x)",          # Differentiation
        "x^2 + y^2",
        "sin(x)",
        "cos(x)",
        "tan(x)",
        "cot(x)",
        "sec(x)",
        "csc(x)",
        "arcsin(x)",
        "arccos(x)",
        "arctan(x)",
        "arccot(x)",
        "arcsec(x)",
        "arccsc(x)",
        "log(x)",
        "ln(x)"
    ]

    for expression in expresions:
        try:
            if expr.startswith("integrate"):
                # Integration example
                inner_expr = expr[10:-3]  # Extract expression from "integrate(...)"
                result = parser.integrate(inner_expr, 'x')
                print(f"Integral of '{inner_expr}' with respect to x: {result}")
            elif expr.startswith("diff"):
                # Differentiation example
                inner_expr = expr[5:-3]  # Extract expression from "diff(...)"
                result = parser.differentiate(inner_expr, 'x')
                print(f"Derivative of '{inner_expr}' with respect to x: {result}")
            else:
                # General expression evaluation
                result = parser.parse_expression(expr, substitutions={'pi': sp.pi, 'e': sp.E, 'i': sp.I})
                print(f"Result of '{expr}': {result}")
        except ValueError as e:
            print(f"Error: {e}")

