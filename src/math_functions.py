import logging
from numbers import Number
import numpy as np

if __name__ == "__main__":
    print("This module is not meant to by run separately")

logger = logging.getLogger(__name__)

def require_numeric_values(func):
    def inner(*args, **kwargs):
        for arg in args:
            if type(arg) != int and type(arg) != float:
                logger.error("Provide numeric values")
                raise TypeError(f"Values must be numeric")
        return func(*args, **kwargs)
    return inner

@require_numeric_values
def sub(lhs: Number, rhs: Number) -> Number:
    return lhs - rhs

@require_numeric_values
def multiply(lhs: Number, rhs: Number) -> Number:
    return lhs * rhs

@require_numeric_values
def divide(lhs: Number, rhs: Number) -> Number:
    if not rhs:
        raise ValueError("Denominator can't be equal to 0")
    return lhs / rhs

@require_numeric_values
def avg(*args):
    return np.average([arg for arg in args])
