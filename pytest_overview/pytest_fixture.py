import pytest


# @pytest.fixture()
@pytest.fixture(autouse=True)
def setup():
    print('\nsetup')


# def test_1(setup):
def test_1():
    print('exec test1')
    assert True


# @pytest.mark.usefixtures('setup')
def test_2():
    print('exec test2')
    assert True
