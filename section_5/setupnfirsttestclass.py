import pytest
from checkout import Checkout

"""
first step
def test_CanInstantiateCheckout():
    co = Checkout()
"""

def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice('a', 1)

def test_CanAddItem():
    co = Checkout()
    co.addItem('a')
