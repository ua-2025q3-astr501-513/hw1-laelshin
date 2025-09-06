import numpy as np
from p3.p3 import quadratic  # adjust import according to your package structure

def test_two_real_roots():
    x1, x2 = quadratic(1, -3, 2)  # x^2 - 3x + 2 = 0
    assert np.isclose(x1, 1)
    assert np.isclose(x2, 2)

def test_one_real_root():
    x1, x2 = quadratic(1, 2, 1)  # x^2 + 2x + 1 = 0
    assert np.isclose(x1, -1)
    assert x2 is None

def test_no_real_root():
    x1, x2 = quadratic(1, 0, 1)  # x^2 + 1 = 0
    assert x1 is None
    assert x2 is None

def test_negative_b_stability():
    x1, x2 = quadratic(1, 1e8, 1)  # check catastrophic cancellation
    # One root should be small, one very large negative
    assert x1 < x2
