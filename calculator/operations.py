"""
Operations
"""
# Importing
from decimal import Decimal

# Defining a function
def add(a: Decimal, b: Decimal) -> Decimal: # Addition
    """Addition"""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal: # Subtraction
    """Subtraction"""
    return a -b

def multiply(a: Decimal, b: Decimal) -> Decimal: # Multiplication
    """Multiplication"""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal: # Division
    """Division"""
    if b == Decimal('0'):
        raise ValueError("Cannot divide by zero.")
    return a / b
