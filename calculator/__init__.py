"""
Calculator Class
"""
# Imports
from calculator.calculations import Calculations # History of calculations
from calculator.operations import add, subtract, multiply, divide # Operations that the calculator will do
from calculator.calculation import Calculation # Only one calculation will be performed at a time
from decimal import Decimal # Decimal value calculations
from typing import Callable# Specification of a function

# Defining the Calculator
class Calculator:
    """Calculator Class"""
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Performs the operation"""
        calculation = Calculation.create(a, b, operation) # Create a calculation object that will be passing in operations
        Calculations.add_calculation(calculation) # Calculations are added to the history
        return calculation.perform() # Calculation will be performed and returned

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Sum"""
        return Calculator._perform_operation(a, b, add) # Addition is going to be performed

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Subtraction"""
        return Calculator._perform_operation(a, b, subtract) # Subtraction is going to be performed

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Multiplication"""
        return Calculator._perform_operation(a, b, multiply) # Multiplication is going to be performed

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Division"""
        return Calculator._perform_operation(a, b, divide) # Division is going to be performed
    