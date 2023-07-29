from calc_session_assignment import *

def test_add_negative_numbers():
    result =add(-2,0)
    assert result == -2

def test_add_positive_numbers():
    result =add(2,3)
    assert result == 5

def test_add_zero():
    result =add(-2,0)
    assert result == -2

def test_divide_by_numbers():
    result =divide(-2,0)
    assert result == 'infinity'


