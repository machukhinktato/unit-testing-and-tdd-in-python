
def setup_module(module):
    print("setting up module")

def teardown_module(module):
    print("teardown_method module")

def setup_function(function):
    if function == test1:
        print("Setting up test1")
    elif function == test2:
        print("Setting up test2")
    else:
        print("Setting up unknown test")

def teardown_function(function):
    if function == test1:
        print("Tearing down test1")
    elif function == test2:
        print("Tearing down test2")
    else:
        print("Tearing down unknown test")


def test1():
    print("Executing test1")
    assert True


def test2():
    print("Executing test2")
    assert True


"""
setting up module
Setting up test1
Executing test1
Tearing down test1
Setting up test2
Executing test2
Tearing down test2
teardown_method module
"""
