import sympy as sp

def expession_to_latex(expression_str):
    """
    Converts a mathematical expression to LaTeX using sympy.

    :param expression_str: A string containing the mathematical expression.
    :return: LaTeX representation of the expression.
    """
    try:
        expression = sp.sympify(expression_str)
        latex_expression = sp.latex(expression)
        return latex_expression
    except (sp.SympifyError,Exception) as e:
        return f"Error in processing expression: {str(e)}"

def detect_math_type(latex_expr: str) -> str:
    """
    Detects the type of mathematical expression.

    :param latex_expr: A string containing the mathematical expression.
    :return: Type of the expression (algebraic, trigonometric, etc.).
    """
    try:
        expression = sp.sympify(latex_expr)

        if expression.is_Polynomial:
            return "Algebraic expression (polynomial)"
        elif expression.is_trigonometric:
            return "Trigonometric function"
        elif isinstance(expression, sp.Derivative):
            return "Derivative (calculus)"
        elif isinstance(expression, sp.Integral):
            return "Integral (calculus)"
        elif expression.is_rational_function:
            return "Rational function"
        elif expression.is_number:
            return "Number"
        elif expression.is_log:
            return "Logarithmic function"
        elif expression.is_exp:
            return "Exponential function"
        elif expression.is_Add:
            return "Addition"
        elif expression.is_Mul:
            return "Multiplication"
        else:
            return "Unknown or unsupported expression type"
    except (sp.SympifyError, Exception) as e:
        return f"Error in detecting expression type: {str(e)}"

def solve_equation(equation):
    """
    Solves a mathematical equation using sympy.

    :param equation: A string containing the equation to solve.
    :return: Solution of the equation.
    """
    try:
        solution = sp.solve(equation)
        return solution
    except (sp.SympifyError, Exception) as e:
        return f"Error in solving equation: {str(e)}"


def solve_equation_step_by_step(equation):
    """
    Solves a mathematical equation step by step using sympy.

    :param equation: A string containing the equation to solve.
    :return: Steps of the solution process.
    """
    try:
        steps = sp.solve(equation, steps=True)
        return steps
    except (sp.SympifyError, Exception) as e:
        return f"Error in solving equation step by step: {str(e)}"