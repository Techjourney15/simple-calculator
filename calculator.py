# BLEAT (Binary, Logarithmic, Exponential, Arithmetic, and Trigonometric) Calculator

import math
from typing import Optional, Union

class BLEATCalculator:
    """Binary, Logarithmic, Exponential, Arithmetic, and Trigonometric Calculator"""

    def __init__(self):
        self.result: Optional[Union[float, int]] = None

    @staticmethod
    def display_menu():
        print("""
..BLEAT CALCULATOR..
Supported Operations:
  Binary Operations:
    +   Addition              -   Subtraction
    *   Multiplication        /   Division
    **  Exponentiation        %   Modulus
  Logarithmic Operations:
    log                      Logarithm (custom base optional)
  Exponential Operations:
    exp                      Exponential (e^x)
  Trigonometric Functions:
    sin, cos, tan            Trigonometric (degrees)
    sinh, cosh, tanh         Hyperbolic
    asin, acos, atan         Inverse Trigonometric (degrees)
  Additional Functions:
    abs                      Absolute Value
    fact                     Factorial
        """)

    def perform_operation(self, num1: float, operator: str, num2: Optional[float] = None) -> Union[float, int]:
        """Performs the operation based on the operator provided."""
        if operator in ["sin", "cos", "tan", "sinh", "cosh", "tanh", "asin", "acos", "atan"]:
            return self.trigonometric_operations(num1, operator)
        elif operator == "log":
            return self.logarithmic_operation(num1)
        elif operator == "exp":
            return math.exp(num1)
        elif operator == "abs":
            return abs(num1)
        elif operator == "fact":
            return self.factorial_operation(num1)
        else:
            return self.binary_operations(num1, operator, num2)

    def trigonometric_operations(self, num1: float, operator: str) -> float:
        """Handles trigonometric and hyperbolic operations."""
        trig_funcs = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sinh": math.sinh,
            "cosh": math.cosh,
            "tanh": math.tanh,
        }
        if operator in trig_funcs:
            return trig_funcs[operator](math.radians(num1)) if operator in ["sin", "cos", "tan"] else trig_funcs[operator](num1)
        if operator == "asin":
            if num1 < -1 or num1 > 1:
                raise ValueError("asin is only defined for values between -1 and 1.")
            return math.degrees(math.asin(num1))
        if operator == "acos":
            if num1 < -1 or num1 > 1:
                raise ValueError("acos is only defined for values between -1 and 1.")
            return math.degrees(math.acos(num1))
        if operator == "atan":
            return math.degrees(math.atan(num1))

    def logarithmic_operation(self, num1: float) -> float:
        """Handles logarithmic operations."""
        base_input = input("Enter the base for the logarithm (leave blank for base e): ").strip()
        base = float(base_input) if base_input else math.e
        if num1 <= 0 or base <= 0 or base == 1:
            raise ValueError("Logarithm undefined for given input.")
        return math.log(num1, base)

    def factorial_operation(self, num1: float) -> int:
        """Handles factorial operations."""
        if num1 < 0 or num1 != int(num1):
            raise ValueError("Factorial is only defined for non-negative integers.")
        return math.factorial(int(num1))

    def binary_operations(self, num1: float, operator: str, num2: Optional[float]) -> float:
        """Handles basic arithmetic and binary operations."""
        if num2 is None:
            raise ValueError("Binary operation requires two numbers.")
        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2
        if operator == "/":
            if num2 == 0:
                raise ValueError("Division by zero is undefined.")
            return num1 / num2
        if operator == "**":
            return num1 ** num2
        if operator == "%":
            return num1 % num2
        raise ValueError("Invalid operator.")

    def start(self):
        """Starts the calculator."""
        while True:
            self.display_menu()
            try:
                num1 = float(input("Enter the first number (or value for single-input operations): "))
                operator = input("Enter the operator: ").strip()
                num2 = None
                if operator not in ["sin", "cos", "tan", "sinh", "cosh", "tanh", "asin", "acos", "atan", "log", "abs", "fact", "exp"]:
                    num2 = float(input("Enter the second number: "))
                self.result = self.perform_operation(num1, operator, num2)
                print(f"Result: {self.result}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

            next_step = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
            if next_step != "yes":
                print("Goodbye! 👋")
                break


# Initialize and run the BLEAT calculator
calculator = BLEATCalculator()
calculator.start()
