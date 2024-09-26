"""
Calculations
"""
# Importing
from decimal import Decimal
from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Addition"""
        cls.history.append(calculation) # Adds the current calculation to the history

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Getting History"""
        return cls.history # Gets the whole history of all the calculations

    @classmethod
    def clear_history(cls):
        """Clearing history"""
        cls.history.clear() # Clears the history of calculations

    @classmethod
    def get_latest(cls) -> Calculation: # Will show the newsest calculations and shows none if there is no history
        """Get the latest from history"""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find by history"""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name] # Returns a list of calculations by the name
    