import pytest


@pytest.fixture(scope="session", autouse=True)
def setupsession():
    print("\nsessions started")

@pytest.fixture(scope="module", autouse=True)
def setupmodule():
    print("\nmodule started")


@pytest.fixture(scope="function", autouse=True)
def setupfunction():
    print("\nfunction started")


def test_1():
    print('exec test1')
    assert True
# @pytest.mark.usefixtures('setup')
def test_2():
    print('exec test2')
    assert True
