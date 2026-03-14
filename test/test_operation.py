from src.math_operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 1) == -1
    assert subtract(-1, -1) == 0
    assert subtract(-5, 5) == -10

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(-5, -5) == 25

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(0, 5) == 0
    assert divide(-10, -5) == 2

    try:
        divide(5, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"        
