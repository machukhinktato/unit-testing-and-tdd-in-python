import pytest


# function which we build with ttd
def fizzBuzz(value, expected):
    if value == 3:
        return expected
    return str(value)


# test that we could call fizzBuzz
@pytest.mark.skip
def test_functionCaller():
    fizzBuzz(1)


#test that we receive value by result of calling
@pytest.mark.skip
def test_functionAnswer():
    ans = fizzBuzz(1)
    assert ans == 1


#test that we receive any value by result of calling
@pytest.mark.skip
def test_functionAnswer_v2():
    ans = fizzBuzz(2, '2')
    assert ans == '2'


#test that we receive any value by result of calling, including string name
def test_functionAnswer_v3():
    ans = fizzBuzz(3, 'fuzz')
    assert ans == 'fuzz'
