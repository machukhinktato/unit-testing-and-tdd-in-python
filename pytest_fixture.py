import pytest

@pytest.fixture
def setup():
    print('setup')

def test_1():
    print('exec test1')
    assert True


def test_2():
    print('exec test2')
    assert True
