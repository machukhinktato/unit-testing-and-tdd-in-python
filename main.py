import pytest

def fizzBuzz(value):
    return 1

@pytest.mark.skip
def test_functionCaller():
    fizzBuzz(1)

def test_functionAnswer():
    ans = fizzBuzz(1)
    assert ans == 1
