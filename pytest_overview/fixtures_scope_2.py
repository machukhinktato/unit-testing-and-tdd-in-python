import pytest


@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nmodule started")

@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nclass started")


@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nfunction started")

class TestClass:
    def test_it(self):
        print('exec test1')
        assert True
    # @pytest.mark.usefixtures('setup')
    def test_it2(self):
        print('exec test2')
        assert True
