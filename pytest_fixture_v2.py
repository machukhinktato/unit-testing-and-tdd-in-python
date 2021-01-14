import pytest


@pytest.fixture()
def setup1():
    print('\nsetup')
    yield
    print('\ntear down 1')


@pytest.fixture()
def setup2(request):
    print('\nsetup2')

    def teardown_a():
        print('\nteardown a')
    def teardown_b():
        print('\nteardown b')

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test_1(setup1):
    print('exec test1')
    assert True
# @pytest.mark.usefixtures('setup')
def test_2(setup2):
    print('exec test2')
    assert True

"""
pytest_fixture_v2.py::test_1
setup
exec test1
PASSED
tear down 1

pytest_fixture_v2.py::test_2
setup2
exec test2
PASSED
teardown b

teardown a
"""
