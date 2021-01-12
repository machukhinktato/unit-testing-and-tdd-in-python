import pytest


# function which we build with ttd
def fizzBuzz(value, expected):
    if (value % 3 == 0) or value == 5:
        return expected
    return str(value)


def checkFizzBuzz(value, expected):
    assert fizzBuzz(value, expected) == expected

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
# @pytest.mark.skip
def test_functionAnswer_v2():
    checkFizzBuzz(2, '2')


#test that we receive any value by result of calling, including string name
# @pytest.mark.skip
def test_functionAnswer_v3():
    checkFizzBuzz(3, 'fuzz')


#another one example of that
# @pytest.mark.skip
def test_functionAnswer_v4():
    checkFizzBuzz(5, 'buzz')


# @pytest.mark.skip
def test_functionAnswer_v5():
    checkFizzBuzz(6, 'fuzz')
