'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

import pytest

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that a subtraction function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that a multiplication function works '''    
    assert multiply(2,2) == 4

def test_division():
    '''Test that a division function works '''    
    assert divide(2,2) == 1

def test_division_by_zero():
    '''Test that division by zero throws a zero division exception'''
    with pytest.raises(ZeroDivisionError):
        divide(1,0)
    