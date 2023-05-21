import pytest
from Basiccalculator import calculator
import math

def test_addition():
    result = calculator(4, '+', 2)
    assert result == 6

def test_subtraction():
    result = calculator(6, '-', 2)
    assert result == 4

def test_multiplication():
    result = calculator(5, '*', 2)
    assert result == 10

def test_division():
    result = calculator(10, '/', 2)
    assert result == 5

def test_invalid_operation():
    result = calculator(5, 'p', 3)
    assert result == 'Invalid operation.'

#To run the code use this in command line: ' pytest test_basic_calculator.py '