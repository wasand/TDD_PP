import pytest
from calc import Calc

num1 = 1
num2 = 2


def test_add():
    assert Calc.add(num1, num2) == 3


def test_int_max():
    assert Calc.int_max(num1, num2) == 2



