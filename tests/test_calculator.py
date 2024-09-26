"""
Calculator Test Module
"""
from decimal import Decimal
from calculator import Calculator

def test_addition():  # Addition Test
    """Addition Operation"""
    assert Calculator.add(Decimal('2'), Decimal('2')) == Decimal('4')  # Confirm

def test_subtraction():  # Subtraction Test
    """Subtraction Operation"""
    assert Calculator.subtract(Decimal('2'), Decimal('2')) == Decimal('0')  # Confirm

def test_divide():  # Division Test
    """Division Operation"""
    assert Calculator.divide(Decimal('2'), Decimal('2')) == Decimal('1')  # Confirm

def test_multiply():  # Multiplication Test
    """Multiplication Test"""
    assert Calculator.multiply(Decimal('2'), Decimal('2')) == Decimal('4')  # Confirm
