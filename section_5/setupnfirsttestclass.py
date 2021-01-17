import pytest
from checkout import Checkout

"""
first step
def test_CanInstantiateCheckout():
    co = Checkout()
"""

@pytest.fixture
def checkout():
    checkout = Checkout()
    return checkout

def test_CanAddItemPrice(checkout):
    # co = Checkout()
    checkout.addItemPrice('a', 1)

def test_CanAddItem(checkout):
    # co = Checkout()
    checkout.addItem('a')

def test_canCalculateTotal(checkout):
    checkout.addItemPrice('a', 1)
    checkout.addItem('a')
    assert checkout.calculateTotal() == 1
    
