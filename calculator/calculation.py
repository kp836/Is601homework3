"""
Calculation Module
"""
# Defining a class so that it can be imported later on
#Importing
from decimal import Decimal # Decimal class is being imported so that decimal operations can be performed
from typing import Callable # Operations will be callable type
from calculator.operations import add, subtract, multiply, divide # Importing arithmetic operations from this module

# Defining a class
class Calculation:
    """Calculation class"""
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]): #type hints for parameters (decimal)
        """Initialization"""
        self.a = a # Initializing the first operation
        self.b = b # Initializing the second operation
        self.operation = operation  # Storing the operation as a callable (takes two decimals and returns one result)

    @staticmethod # New instance of calculation
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Calculation Instance"""
        return Calculation(a, b, operation) # Returns a new object

    def perform(self) -> Decimal: # Method to perform calculation in this particular object
        """Performs the operation"""
        return self.operation(self.a, self.b) # The values taken are operated on and returns the value

    def __repr__(self): # Provides a string representation of the calculation
        """Returns a string"""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})" # Gives a string representation of the calculation
    