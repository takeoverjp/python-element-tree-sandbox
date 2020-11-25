# -*- coding: utf-8 -*-

import pytest
from python_element_tree_sandbox.skeleton import fib

__author__ = "Kondo Takeo"
__copyright__ = "Kondo Takeo"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
