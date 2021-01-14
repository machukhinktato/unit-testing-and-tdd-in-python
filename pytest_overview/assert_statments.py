import pytest
from pytest import approx
from pytest import raises


def test_IntAssert():
    assert 1 == 1

def test_StrAssert():
    assert 'str' == 'str'

def test_FloatAssert():
    assert 1.0 == 1.0

def test_ArrAssert():
    assert [1,2,3] == [1,2,3]

def test_DictAssert():
    assert {'1':1} == {'1':1}

def test_floAt():
    assert (0.1 + 0.2) == approx(0.3)


def raisesValueException():
    # pass
    raise ValueError

def test_exception():
    with raises(ValueError):
        raisesValueException()
