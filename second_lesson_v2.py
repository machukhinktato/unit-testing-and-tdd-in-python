import pytest


class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass")


    def setup_method(self, method):
        if method == self.test1:
            print("Setting up test1")
        elif method == self.test2:
            print("Setting up test2")
        else:
            print("Setting up unknown test")

    def teardown_method(self, method):
        if method == self.test1:
            print("Tearing down test1")
        elif method == self.test2:
            print("Tearing down test2")
        else:
            print("Tearing down unknown test")


    def test1(self):
        print("Executing test1")
        assert True


    def test2(self):
        print("Executing test2")
        assert True

"""
Setup TestClass
Setting up test1
Executing test1
.Tearing down test1
Setting up test2
Executing test2
.Tearing down test2
Teardown TestClass
"""
