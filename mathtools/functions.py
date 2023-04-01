import numpy as np
from numbers import Number
from . import utils

@utils.require_numeric_values
def sub(lhs: Number, rhs: Number) -> Number:
    return lhs - rhs

@utils.require_numeric_values
def multiply(lhs: Number, rhs: Number) -> Number:
    return lhs * rhs

@utils.require_numeric_values
def divide(lhs: Number, rhs: Number) -> Number:
    if not rhs:
        raise ValueError("Denominator can't be equal to 0")
    return lhs / rhs

@utils.require_numeric_values
def avg(*args):
    return np.average([arg for arg in args])