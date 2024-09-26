"""
Calculations Test Module
"""
# Importing
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture # Initialize a test environment
def setup_calculations():
    """Calculation History Setup"""
    Calculations.clear_history() # Clear any existing calculation history
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add)) # Typical use case to verify the history functionality
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract)) # Typical use case to verify the history functionality

def test_add_calculation(setup_calculations):
    """Test Addition History"""
    calc = Calculation(Decimal('2'), Decimal('2'), add) # New calculation object for the history
    Calculations.add_calculation(calc) # Add the calculation
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history" # Confirm if the calculation in the history matches the one added

def test_get_history(setup_calculations):
    """Test History Retrieval"""
    history = Calculations.get_history() # Get the calculation history
    assert len(history) == 2, "History does not contain the expected number of calculations" # Confirm that history has only two calculations matching the fixture setup

def test_clear_history(setup_calculations):
    """Clearing the history"""
    Calculations.clear_history() # Clear the history
    assert len(Calculations.get_history()) == 0, "History was not cleared" # Confirm the history is empty after checking the length

def test_get_latest(setup_calculations):
    """Latest calculation history"""
    latest = Calculations.get_latest() # Get the newest calculation from the history
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation" # Confirm that the newest calculation matches the expected result

def test_find_by_operation(setup_calculations):
    """By operation type"""
    add_operations = Calculations.find_by_operation("add") # Find calculations with the add operand
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation" # confirm that only one calculation with add operation
    subtract_operations = Calculations.find_by_operation("subtract") # Find calculations with the subtract operand
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation" # Confirm that only one calculation with subtraction operation

def test_get_latest_with_empty_history():
    """Latest calculation history with an empty history"""
    Calculations.clear_history() # Confirm if the history clears by itself
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history" # Confirm that the newest calculation is None because the history is empty
