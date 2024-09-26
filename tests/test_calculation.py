"""
Test Calculation Module
"""
# Importing
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# Testing
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')), # Addition
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')), # Subtraction
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')), # Multiplication
    (Decimal('10'), Decimal('2'), divide, Decimal('5')), # Division
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')), # Addition with decimals
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')), # Subtraction with decimals
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')), # Multiplication with decimals
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')), # Division with decimals
])

def test_calculation_operations(a, b, operation, expected):
    """Test different operations using this class"""
    calc = Calculation(a, b, operation) # Calculation instance is given with operation
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}" # Confirm if the result matches with the expected output

def test_calculation_repr():
    """String representation"""
    calc = Calculation(Decimal('10'), Decimal('5'), add) # Calculation instance for testing
    expected_repr = "Calculation(10, 5, add)" # Expected string representation
    assert calc.__repr__() == expected_repr, "The __repr__ method result does not match with the expected string." # Confirm that the string representation matches the string result.

def test_divide_by_zero():
    """Dividing by zero test"""
    calc = Calculation(Decimal('10'), Decimal('0'), divide) # Calculation instance with zero divisor
    with pytest.raises(ValueError, match="Cannot divide by zero"): # Expect a ValueError to be raised
        calc.perform() # Will try to do the calculation but it will show ValueError
