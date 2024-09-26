"""
Tests for operations
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    """Addition Test"""
    calculation = Calculation(Decimal('10'), Decimal('5'), add)  # Addition Operation
    assert calculation.perform() == Decimal('15'), "Add operation failed"  # Confirm

def test_operation_subtract():
    """Subtraction Test"""
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)  # Subtraction Operation
    assert calculation.perform() == Decimal('5'), "Subtract operation failed"  # Confirm

def test_operation_multiply():
    """Multiplication Test"""
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)  # Multiplication Operation
    assert calculation.perform() == Decimal('50'), "Multiply operation failed"  # Confirm

def test_operation_divide():
    """Division Test"""
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)  # Division Operation
    assert calculation.perform() == Decimal('2'), "Divide operation failed"  # Confirm

def test_divide_by_zero():
    """Division by zero test"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Cannot divide by zero operation
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()  # This should raise an exception
